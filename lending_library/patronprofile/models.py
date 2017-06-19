from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
import uuid

# Create your models here.


class PatronProfile(models.Model):
    """A profile for users to our application."""

    user = models.OneToOneField(User)
    library_card_id = models.UUIDField(default=uuid.uuid4, editable=False)

    def __repr__(self):
        return self.user.username


@receiver(post_save, sender=User)
def make_profile_for_new_user(sender, **kwargs):
    if kwargs['created']:
        new_profile = PatronProfile(
            user=kwargs['instance']
        )
        new_profile.save()