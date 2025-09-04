from django.db import models

class Contact(models.Model):
    name = models.CharField(max_lenght=100)
    email = models.EmailField()
    submitted_at = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"