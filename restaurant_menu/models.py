from django.contrib.auth.models import User
from django.db import models


MEAL_TYPE = (
    ('starters', 'Starters'),
    ('drinks', 'Drinks'),
    ('main_dishes', 'Main Dishes'),
    ('salads', 'Salads'),
    ('desserts', 'Desserts'),
)

STATUS = (
    (1, 'Available'),
    (0, 'Unavailable'),
)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    ingredients = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal