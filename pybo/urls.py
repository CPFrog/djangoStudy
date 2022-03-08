from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views

# 3-11장에서 views.py를 각 게시글 종류에 따라 역할을 담당하는 여러개의 *_views.py 파일로 나눔에 따라 참조 위치도 바뀜.

app_name = 'pybo'

urlpatterns = [
    # views -> base_views : 기초
    path('', base_views.index, name='index'),  # URL 별칭-->index
    path('<int:question_id>/', base_views.detail, name='detail'),  # URL 별칭-->detail

    # views -> question_views : 질문 게시글 관련
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>', question_views.question_delete, name='question_delete'),

    # views -> answer_views : 답변 게시글 관련
    path('answer/create/<int:question_id>', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>', answer_views.answer_delete, name='answer_delete'),

    # views -> comment_views : 댓글 관련
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question,
         name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question,
         name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

    # views -> vote_views : 게시글 추천 관련
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]
