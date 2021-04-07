from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Questboard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    stars = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    is_for_everyone = models.BooleanField(default=False)
    student1 = models.CharField(max_length=100, blank=True)
    student2 = models.CharField(max_length=100, blank=True)
    student3 = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '{}: {} star(s)'.format(self.name, self.stars)