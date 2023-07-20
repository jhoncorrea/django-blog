from django.db import models
from django.db.models.fields import CharField, URLField, DateField
from django.db.models.fields.files import ImageField
from datetime import date


# Create your models here.
class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
    date = DateField(default=date.today)

    #con esto lo muestro en el admin con el titulo y sin el Project object (1)
    def __str__(self) -> str:
        return self.title
    