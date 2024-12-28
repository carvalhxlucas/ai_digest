from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Painel admin
    path('', include('newsletter.urls')),  # Inclui as URLs do app newsletter
]
