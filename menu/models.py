from django.db import models

# Create your models here.
from user.models import User


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MenuItem(models.Model):
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)


