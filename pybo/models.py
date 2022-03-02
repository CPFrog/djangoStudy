from django.db import models
from django.contrib.auth.models import User


# Q&A 게시판 생성

# 질문 게시글에 필요한 내용
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # 익명질문이 가능하도록 질문 작성자에 null이 들어갈 수 있도록 함.
    subject = models.CharField(max_length=200)  # 질문 제목
    content = models.TextField()  # 질문 내용
    create_date = models.DateTimeField()  # 게시글 작성 시각
    modify_date = models.DateTimeField(null=True, blank=True)  # 최종 수정 시각. 수정 안해서 null값을 가질 수 있으므로 이를 허용.

    def __str__(self):
        return self.subject


# 답변 게시글에 필요한 내용
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 답변 작성자
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 답변을 달 질문 게시글 정보, 질문 게시글 삭제시 답변도 삭제.
    content = models.TextField()  # 답변 내용
    create_date = models.DateTimeField()  # 답변 게시글 작성 시각
    modify_date = models.DateTimeField(null=True, blank=True)  # 최종 수정 시각. 수정 안해서 null값을 가질 수 있으므로 이를 허용.


# 댓글 기능 구현에 필요한 클래스
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 댓글 작성자
    content = models.TextField()  # 댓글 내용
    create_date = models.DateTimeField()  # 댓글 작성 시각
    modify_date = models.DateTimeField(null=True, blank=True)  # 수정 시각
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)  # 이 댓글이 달린 질문
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)  # 이 댓글이 달린 답변
