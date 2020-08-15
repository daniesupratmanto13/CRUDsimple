from django.urls import path
from . import views

app_name = 'data'

urlpatterns = [
    path('delete/<int:idInput>/', views.delete, name='delete'),
    path('update/<int:idInput>', views.update, name='update'),
    # path('create/', views.create, name='create'),
    path('', views.index, name='index')
]
