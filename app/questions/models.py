from django.db import models
from skills.models import Skill


class Question(models.Model):
    statement = models.TextField(blank=False, null=False)
    option_a = models.TextField()
    option_b = models.TextField()
    option_c = models.TextField()
    option_d = models.TextField()
    option_e = models.TextField()
    