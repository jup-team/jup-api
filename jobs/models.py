from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Job(models.Model):

    SENIORITY = (
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

    seniority = models.CharField(choices=OPTIONS, default='PLENO')
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    description = models.TextField(max_length=500)
    location = CharField()
    owner = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='CRIADA') 
    contract_type = models.CharField(choices=CONTRACTS)
    start_pub = models.DateField()
    end_pub = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
