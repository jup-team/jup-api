from rest_framework import viewsets, status, mixins
from .models import Skill
from .serializers import SkillSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get']

    @method_decorator(cache_page(3600))
    def dispatch(self, *args, **kwargs):
        return super(SkillsViewSet, self).dispatch(*args, **kwargs)
