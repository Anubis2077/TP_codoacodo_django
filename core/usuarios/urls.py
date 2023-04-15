from django.contrib import admin
from django.urls import path
from core.usuarios.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', IndexView.as_view(),name='index_cxm'),
    path('register/', Register_index.as_view(), name='register'),
    path('login/', Login_index.as_view(), name='login'),
    path('home/', LoginView.as_view(template_name='home.html'), name='home'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)