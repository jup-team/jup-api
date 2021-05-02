from .views import SkillsViewSet
from django.urls import re_path

urlpatterns = [
    re_path(r'^skills/?$', SkillsViewSet.as_view({'get': 'get_skills'}), name='get_skills'),
]
