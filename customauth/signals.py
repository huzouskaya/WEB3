from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, MyUser 


@receiver(post_save, sender=MyUser )
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=MyUser )
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.userprofile.save()
    except UserProfile.DoesNotExist:
        # Optionally log this case or handle it
        pass

# @receiver(post_save, sender=MyUser )
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()