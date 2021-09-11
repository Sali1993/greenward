from django.urls import path
from . import views

urlpatterns = [
    path('', views.local_list, name='local_list'),
    path('locals/<int:pk>', views.local_detail, name='local_detail'),
    path('local/new', views.local_create, name='local_create'),
    path('locals/<int:pk>/edit', views.local_edit, name='local_edit'),
    path('locals/<int:pk>/delete', views.local_delete, name='local_delete'),
]
