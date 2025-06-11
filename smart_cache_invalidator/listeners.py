from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .signals import cache_invalidation_signal
from .utils import invalidate_cache

@receiver(post_save)
def handle_post_save(sender, instance, **kwargs):
    # Invalidate cache when a model instance is saved
    invalidate_cache(instance)

@receiver(post_delete)
def handle_post_delete(sender, instance, **kwargs):
    # Invalidate cache when a model instance is deleted
    invalidate_cache(instance)

@receiver(cache_invalidation_signal)
def handle_cache_invalidation(sender, **kwargs):
    # Custom logic for handling cache invalidation signals
    invalidate_cache(kwargs.get('instance'))