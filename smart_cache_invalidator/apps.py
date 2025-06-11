from django.apps import AppConfig

class SmartCacheInvalidatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cache_invalidator'
    verbose_name = 'Smart Cache Invalidator'