from celery import shared_task

@shared_task
def invalidate_cache(key):
    """
    Invalidate the cache for the given key.
    This task can be called asynchronously to clear cache entries.
    """
    # Logic to invalidate the cache
    pass

@shared_task
def bulk_invalidate_cache(keys):
    """
    Invalidate the cache for a list of keys.
    This task can be called asynchronously to clear multiple cache entries.
    """
    for key in keys:
        invalidate_cache(key)