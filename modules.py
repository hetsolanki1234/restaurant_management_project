from django.db import modules
from django.contib.auth.models import User

class Profile(modules.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_lenght=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Menu(models.Model):
    name = models.CharField(max_lenght=100)
    price = models.DecimalField(max_digits=8,decimal_place=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
    ]  

    customer = models.ForeignKey(User, on_delete=models.CASCADE,related_name="orders"
    order_item = models.ManyToManyField(Menu, related_name="orders")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_lenght=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DataTimeField(auto_now_add = True)
    updated_at = models.DataTimeField(auto_now = True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username} ({self.status})"
