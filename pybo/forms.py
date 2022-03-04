from django import forms
from pybo.models import Question, Answer, Comment


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']  # 임의로 '질문 제목', '질문 내용' 썼더니 에러뜸.
        # # form.as_p 로 생성한 질문 양식에 부트스트랩 적용하는 코드
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }

        # subject, content를 다른 이름으로 보이기 위한 코드
        labels = {
            'subject': '제목',
            'content': '질문 내용',
        }


# 답변 작성에 대한 양식 생성 코드
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용',  # 내용 라벨을 한국어로 보이게 하기 위한 코드
        }


# 댓글 작성 양식 생성 코드
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글 내용'  # 내용 라벨을 한국어로 보이게 하기 위한 코드
        }
