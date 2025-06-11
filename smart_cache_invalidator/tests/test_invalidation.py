import pytest
from smart_cache_invalidator.utils import invalidate_cache

def test_invalidate_cache():
    # Assuming we have a cache set up and a key to invalidate
    cache_key = 'test_key'
    
    # Set a value in the cache
    cache.set(cache_key, 'test_value')
    
    # Ensure the value is set
    assert cache.get(cache_key) == 'test_value'
    
    # Invalidate the cache
    invalidate_cache(cache_key)
    
    # Ensure the value is invalidated
    assert cache.get(cache_key) is None

def test_invalidate_non_existent_cache():
    # Test invalidating a cache key that doesn't exist
    cache_key = 'non_existent_key'
    
    # Ensure the value is None before invalidation
    assert cache.get(cache_key) is None
    
    # Invalidate the non-existent cache
    invalidate_cache(cache_key)
    
    # Ensure the value is still None
    assert cache.get(cache_key) is None