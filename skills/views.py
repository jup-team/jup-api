from rest_framework import viewsets, status, mixins
from .models import Skill
from .serializers import SkillSerializer


class SkillsViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
