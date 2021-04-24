from django.urls import re_path
from users.views import LoginViewSet


urlpatterns = [
    re_path(r'^sign-up/?$', LoginViewSet.as_view({'post': 'sign_up'}), name='sign_up'),
    re_path(r'^sign-in/?$', LoginViewSet.as_view({'post': 'sign_in'}), name='sign_in'),
]
