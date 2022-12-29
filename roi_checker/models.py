from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField


class college(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    fees = models.DecimalField(max_digits=5,decimal_places=2)
    average = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)
    median = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)

    class Meta:
        verbose_name_plural = "College"

    def __str__(self):
        return self.name
