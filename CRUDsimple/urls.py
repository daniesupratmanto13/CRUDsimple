from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('data/', include('data.urls')),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
