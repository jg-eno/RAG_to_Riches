"""API key load balancing functionality."""
import os
from dotenv import load_dotenv
import threading
import random

class ApiKeyLoadBalancer:
    """Load balancer for API keys using Round Robin technique."""
    
    def __init__(self, key_prefix="GEMINI_API_KEY", num_keys=5):
        """Initialize the load balancer.
        
        Args:
            key_prefix: The prefix for API keys in the .env file
            num_keys: The number of API keys available
        """
        # Load environment variables
        load_dotenv()
        
        # Get API keys
        self.api_keys = []
        for i in range(1, num_keys + 1):
            key_name = f"{key_prefix}_{i}"
            key = os.getenv(key_name)
            if key:
                self.api_keys.append(key)
        
        if not self.api_keys:
            raise ValueError(f"No API keys found with prefix {key_prefix}")
        
        # Initialize current key index
        self.current_index = 0
        
        # Thread lock for thread safety
        self.lock = threading.Lock()
        
        # Track last used key to ensure change
        self.last_used_key = None
        
        print(f"API Key Load Balancer initialized with {len(self.api_keys)} keys")
    
    def get_next_key(self):
        """Get the next API key, ensuring it's different from the last used key.
        
        Returns:
            str: The next API key
        """
        with self.lock:
            # If we only have one key, just return it
            if len(self.api_keys) == 1:
                return self.api_keys[0]
            
            # If we have multiple keys, ensure we don't use the same key twice in a row
            if len(self.api_keys) > 1:
                # Get available keys (excluding the last used key)
                available_keys = [key for key in self.api_keys if key != self.last_used_key]
                
                # If somehow all keys were used (shouldn't happen with our implementation)
                # or this is the first request, use standard round-robin
                if not available_keys:
                    key = self.api_keys[self.current_index]
                    self.current_index = (self.current_index + 1) % len(self.api_keys)
                else:
                    # Randomly select from available keys for better distribution
                    key = random.choice(available_keys)
                    
                    # Update the index to match the selected key for next round-robin continuation
                    self.current_index = self.api_keys.index(key)
                    self.current_index = (self.current_index + 1) % len(self.api_keys)
            
            # Remember this key as the last used
            self.last_used_key = key
            
            return key

# Singleton instance
_load_balancer = None

def get_load_balancer():
    """Get the singleton load balancer instance."""
    global _load_balancer
    if _load_balancer is None:
        _load_balancer = ApiKeyLoadBalancer()
    return _load_balancer

def get_api_key():
    """Get the next API key from the load balancer."""
    return get_load_balancer().get_next_key()
