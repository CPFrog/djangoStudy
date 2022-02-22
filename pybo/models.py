from django.db import models


# Q&A 게시판 생성

# 질문 게시글에 필요한 내용
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 질문 제목
    content = models.TextField()  # 질문 내용
    create_date = models.DateTimeField()  # 게시글 작성 시각

    def __str__(self):
        return self.subject


# 답변 게시글에 필요한 내용
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 답변을 달 질문 게시글 정보, 질문 게시글 삭제시 답변도 삭제.
    content = models.TextField()  # 답변 내용
    create_date = models.DateTimeField()  # 답변 게시글 작성 시각
