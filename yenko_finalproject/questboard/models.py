from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class QuestCard(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    stars = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    is_for_everyone = models.BooleanField(
        default=False,
        verbose_name="The Quest is for Everyone"
    )
    student1 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="First Student"
    )
    student2 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Second Student"
    )
    student3 = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Third Student"
    )

    def __str__(self):
        return '{}: {} star(s)'.format(self.name, self.stars)

    @property
    def stars_range(self):
        return range(self.stars)