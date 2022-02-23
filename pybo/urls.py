from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),  # URL 별칭-->index
    path('<int:question_id>/', views.detail, name='detail'),  # URL 별칭-->detail
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
