"""API key load balancing functionality."""
import os
from dotenv import load_dotenv
import threading

class ApiKeyLoadBalancer:
    """Load balancer for API keys using Round Robin technique."""
    
    def __init__(self, key_prefix="GEMINI_API_KEY", num_keys=4):
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
        
        print(f"API Key Load Balancer initialized with {len(self.api_keys)} keys")
    
    def get_next_key(self):
        """Get the next API key using Round Robin.
        
        Returns:
            str: The next API key
        """
        with self.lock:
            # Get the current key
            key = self.api_keys[self.current_index]
            
            # Move to the next key for the next request
            self.current_index = (self.current_index + 1) % len(self.api_keys)
            
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
