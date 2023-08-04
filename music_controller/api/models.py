from django.db import models
import string
import random


def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choice(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    
    return code


# Create your models here.
class Room(models.Model):
    # Room model Fields
    # Models documentation: https://docs.djangoproject.com/en/4.2/topics/db/models/
    # Setting Primary Keys: https://docs.djangoproject.com/en/4.2/topics/db/models/#automatic-primary-key-fields
    code = models.CharField(max_length=8, default='', unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    # Read documentation
    # Model meta options: https://docs.djangoproject.com/en/4.2/topics/db/models/#meta-options
    class Meta:
        db_table = "rooms"
