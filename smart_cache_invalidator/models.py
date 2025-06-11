from django.db import models

class CacheInvalidation(models.Model):
    key = models.CharField(max_length=255, unique=True)
    invalidated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"CacheInvalidation(key={self.key}, invalidated_at={self.invalidated_at})"