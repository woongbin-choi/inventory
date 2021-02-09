from django.urls import path
from .views import controlbase_views, takeout_views

app_name = 'control'

urlpatterns = [
    path('', controlbase_views.indexB, name='indexB'),
    path('<int:takeout_id>/', controlbase_views.detail, name='detail'),
    path('takeout/create/', takeout_views.takeout_create, name='takeout_create'),
    path('takeout/modify/<int:takeout_id>/', takeout_views.takeout_modify, name='takeout_modify'),
    path('takeout/delete/<int:takeout_id>/', takeout_views.takeout_delete, name='takeout_delete'),
]
