from django.db import models
from django.core.validators import MaxValueValidator
from skills.models import Skill
from django.contrib.auth.models import User


class Question(models.Model):
    OPTIONS = (
        ('A', 'opção A'),
        ('B', 'opção B'),
        ('C', 'opção C'),
        ('D', 'opção D'),
        ('E', 'opção E'),
    )

    LEVELS = (
        (1, 'Básico'),
        (2, 'Intermediário'),
        (3, 'Avançado'),
    )
    statement = models.TextField()
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField(blank=True, null=True)
    option_d = models.TextField(blank=True, null=True)
    option_e = models.TextField(blank=True, null=True)
    correct_option = models.CharField(max_length=1, choices=OPTIONS, blank=False, null=False, default='A')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField(validators=[MaxValueValidator(1)], choices=LEVELS, blank=False, null=False, default=1)
    creator = models.ForeignKey(User, null=False, blank=False, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.statement
