from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf.urls.static import static
from setup.settings import settings
from challengenews.views import SignUpCreateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Jungledevs-challenge API",
      default_version='v1',
      description="Challenge #001",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="scp2@cin.ufpe.br"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('control-panel/', admin.site.urls),
    path('api/login/', views.obtain_auth_token),
    path('api/sign-up/', SignUpCreateView.as_view(), name='sing-up'),
    path('api/', include('challengenews.urls'), name='api'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
