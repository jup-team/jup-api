from django.urls import re_path
from .views import JobsViewSet


urlpatterns = [
    re_path(r'^jobs-list/?$', JobsViewSet.as_view({'get': 'get_jobs_card'}), name='get_jobs_card'),
]
