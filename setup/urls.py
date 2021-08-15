from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from django.conf.urls.static import static
from setup.settings import settings
from challengenews.views import SignUpCreateView


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('control-panel/', admin.site.urls),
    path('api/login/', views.obtain_auth_token),
    path('api/sign-up/', SignUpCreateView.as_view(), name='sing-up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
