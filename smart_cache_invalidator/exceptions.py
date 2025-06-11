class CacheInvalidationError(Exception):
    """Base class for exceptions related to cache invalidation."""
    pass

class CacheKeyNotFoundError(CacheInvalidationError):
    """Exception raised when a cache key is not found."""
    pass

class CacheInvalidationFailedError(CacheInvalidationError):
    """Exception raised when cache invalidation fails."""
    pass

class InvalidCacheConfigurationError(CacheInvalidationError):
    """Exception raised for invalid cache configuration."""
    pass