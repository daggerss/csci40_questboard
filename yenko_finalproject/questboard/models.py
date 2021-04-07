from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class QuestBoard(models.Model):
    subject_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    required_stars = models.IntegerField(default=1,
        validators=[
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return self.subject_name

    def get_absolute_url(self):
        return reverse('board-detail', kwargs={'id': self.id})


class QuestCard(models.Model):
    subject = models.ForeignKey(
        QuestBoard,
        on_delete=models.CASCADE,
        related_name='quests'
    )
    quest_name = models.CharField(max_length=100)
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
        return '{}: {}'.format(self.subject.subject_name, self.quest_name)

    @property
    def stars_range(self):
        return range(self.stars)