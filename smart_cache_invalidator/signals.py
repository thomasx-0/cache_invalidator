from django.dispatch import Signal

# Define a custom signal for cache invalidation
cache_invalidated = Signal(providing_args=["instance", "cache_key"])

# Example receiver function
def invalidate_cache_receiver(sender, instance, cache_key, **kwargs):
    # Logic to invalidate the cache
    pass

# Connect the signal to the receiver
cache_invalidated.connect(invalidate_cache_receiver)