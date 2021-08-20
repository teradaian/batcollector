from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name="about"),
  path('bats/', views.bats_index, name='bats_index'),
  path('bats/<int:bat_id>/', views.bat_details, name='bat_details'),
  path('bats/create/', views.BatCreate.as_view(), name='bats_create'),
  path('bats/<int:pk>/update/', views.BatUpdate.as_view(), name='bats_update'),
  path('bats/<int:pk>/delete/', views.BatDelete.as_view(), name='bats_delete'),
  path('bats/<int:bat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]


