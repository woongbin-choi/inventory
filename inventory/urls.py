from django.urls import path

from .views import base_views, management_views


app_name = 'inventory'

urlpatterns = [

    path('', base_views.index, name='index'),
    path('<int:management_id>/', base_views.detail, name='detail'),
    path('management/create/', management_views.management_create, name='management_create'),
    path('management/modify/<int:management_id>/', management_views.management_modify, name='management_modify'),
    path('management/delete/<int:management_id>/', management_views.management_delete, name='management_delete'),
]

