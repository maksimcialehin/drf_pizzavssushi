from django.db import models
from django.core.validators import RegexValidator


class Pizzeria(models.Model):
    restaurant_name = models.CharField(max_length=200, blank=False)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.IntegerField(blank=True, default=0)
    website = models.URLField(max_length=420, blank=True)
    phone_number = models.CharField(
        validators=[RegexValidator(regex=r'^\1?\d{9,10}$')],
        max_length=10,
        blank=True
        )
    description = models.TextField(blank=True)
    logo_image = models.ImageField(
        upload_to='pizzeriaImage',
        blank=True,
        default='pizzeriaImage/pizzalogo.png'
    )
    email = models.EmailField(max_length=120, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.restaurant_name}, {self.street}'
