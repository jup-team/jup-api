from django.db import models
from users.models import User


class Position(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Job(models.Model):
    SENIORITIES = (
        ('ESTAGIARIO', 'Estagiário'),
        ('JUNIOR', 'Júnior'),
        ('PLENO', 'Pleno'),
        ('SENIOR', 'Sênior'),
    )

    STATUS = (
        ('CRIADA', 'Criada'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('ENCERRADA', 'Encerrada'),
    )

    CONTRACTS = (
        ('PJ', 'PJ'),
        ('CLT', 'CLT')
    )

    seniority = models.CharField(choices=SENIORITIES, default='PLENO', max_length=25)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    description = models.TextField(max_length=500)
    location = models.CharField(max_length=30)
    owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='CRIADA', max_length=20) 
    contract_type = models.CharField(choices=CONTRACTS, max_length=15)
    start_pub = models.DateField()
    end_pub = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
