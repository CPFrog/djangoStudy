from django.db import models
from django.contrib.auth.models import User


# Q&A 게시판 생성

# 질문 게시글에 필요한 내용
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='question_author')
    # 익명질문이 가능하도록 질문 작성자에 null이 들어갈 수 있도록 함.
    # voter와 author가 동일하게 User 모델을 참조하기 때문에 어떤 필드를 우선 참조할지 결정하라는 오류 뜸 --> author_question 옵션 지정으로 해결
    subject = models.CharField(max_length=200)  # 질문 제목
    content = models.TextField()  # 질문 내용
    create_date = models.DateTimeField()  # 게시글 작성 시각
    modify_date = models.DateTimeField(null=True, blank=True)  # 최종 수정 시각. 수정 안해서 null값을 가질 수 있으므로 이를 허용.
    voter = models.ManyToManyField(User, related_name='question_voter')  # 추천한 사람 필드 추가

    # 하나의 질문에 여러 사람이 추천할 수 있고, 여러 사람이 하나의 질문 추천할 수 있으므로 다대다 필드로 설정.

    def __str__(self):
        return self.subject


# 답변 게시글에 필요한 내용
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_author')  # 답변 작성자
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 답변을 달 질문 게시글 정보, 질문 게시글 삭제시 답변도 삭제.
    content = models.TextField()  # 답변 내용
    create_date = models.DateTimeField()  # 답변 게시글 작성 시각
    modify_date = models.DateTimeField(null=True, blank=True)  # 최종 수정 시각. 수정 안해서 null값을 가질 수 있으므로 이를 허용.
    voter = models.ManyToManyField(User, related_name='answer_voter')


# 댓글 기능 구현에 필요한 클래스
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자
    content = models.TextField()  # 댓글 내용
    create_date = models.DateTimeField()  # 댓글 작성 시각
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정 시각
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)  # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)  # 이 댓글이 달린 답변
