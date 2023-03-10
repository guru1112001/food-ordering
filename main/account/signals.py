from django.db.models.signals import post_save #post save "save the object at that time"
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Customer
# # this function send a signals whenever customer  is created 
# #  instance is the actual object that has just been saved and triggered the post_save signal

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Customer.objects.create(user=instance,
        name=instance.username,
        email=instance.email
        )



post_save.connect(create_profile, sender=User)