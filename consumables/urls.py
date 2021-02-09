from django.urls import path
from .views import basic_views, question_views

app_name = 'consumables'
# path('consumables/', basic_views.index, name='index'),
urlpatterns = [
    path('', basic_views.indexA, name='indexA'),
    path('<int:question_id>/', basic_views.detail, name='detail'),
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
]
