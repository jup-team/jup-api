from django.db import models


class Skill(models.Model):
    title = models.CharField(null=False, blank=False, max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title