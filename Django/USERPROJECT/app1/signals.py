'''
from django.contrib.auth.models import User
from django.db.models.signals import post_save ,post_delete
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user =instance)
        print("Profile has been created successfully....!")

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    try: 
        instance.profile.save()
        print("Profile has been updated")
    except:
        Profile.objects.create(user=instance)
        print("Profile has been created for existing user successfully....!")

def profile_delete_signal(sender,instance,**kwargs):
    print(sender, instance, "--------------------------------")
    print(f"Hello {instance.user.username}--- Unfortunately ur profile has deleted...!")

post_delete.connect(profile_delete_signal, sender=Profile)

'''
# Custom signals
from django.dispatch import Signal, receiver

ping_signal = Signal(providing_args=['context'])

class SignalDemo:
    def ping(self):
        print('PING')
        ping_signal.send(sender=SignalDemo, flag = True)

@receiver(ping_signal, sender=SignalDemo)
def pong(**kwargs):
    if kwargs['flag'] :
        print("PONG")
    # print(kwargs)
        
s1 = SignalDemo()
s1.ping()