from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User,Profile
@receiver(post_save, sender=User)
def create_profile_after_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)