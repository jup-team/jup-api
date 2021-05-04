from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from jobs.views import PositionViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Jup API",
        default_version="v1",
        description="Swagger for JUP API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)
router = DefaultRouter()
router.register(r'positions', PositionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('users.urls', 'user'), namespace='user')),
    path('jobs/', include(('jobs.urls', 'jobs'), namespace='jobs')),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
