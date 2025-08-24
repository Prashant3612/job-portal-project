# accounts/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile, Location, Role

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)

        # Set default ManyToMany field after creation
        default_location = Location.objects.filter(name="Remote").first()
        if default_location:
            profile.preferred_location.add(default_location)
        default_role = Role.objects.filter(name="sql developer").first()
        if default_role:
            profile.preferred_role.add(default_role)
