from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.conf import settings


class Statement(models.Model):
    id = models.IntegerField(primary_key=True)
    capibara_format = models.CharField(max_length=255)
    capibara_slang = models.CharField(max_length=255)
    capibara_phrases = models.JSONField()

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
