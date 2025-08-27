from django.db import modules
from django.contib.auth.models import User

class Profile(modules.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_lenght=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
