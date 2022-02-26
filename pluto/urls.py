from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('test/', views.test, name='test'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('form_upload/', views.model_form_upload, name='model_form_upload'),
    path('thee_admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)