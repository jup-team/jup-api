from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from jobs.views import PositionViewSet

router = DefaultRouter()
router.register(r'positions', PositionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('users.urls', 'user'), namespace='user')),
    path('jobs/', include(('jobs.urls', 'jobs'), namespace='jobs')),
    path('', include(router.urls))
]
