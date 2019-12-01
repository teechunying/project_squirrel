from django.urls import path
from . import views
app_name = 'squirrel'
urlpatterns = [
        path('',views.main_list,name='main_list'),
        path('add/',views.add, name='add'),
        path('stats/',views.stats,name='stats'),
        path('<str:unique_squirrel_id>/', views.update_delete,name='update_delete'),
        path('<str:unique_squirrel_id>/delete', views.delete, name='delete'),
        ]

