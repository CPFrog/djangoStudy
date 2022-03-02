from django import forms
from pybo.models import Question, Answer


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


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용',
        }
