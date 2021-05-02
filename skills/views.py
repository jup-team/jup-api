from rest_framework import viewsets, status, mixins
from .models import Skill
from .serializers import SkillSerializer


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get']
