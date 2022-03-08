from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..models import Answer
from ..forms import AnswerForm


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """ pybo 답변 등록 """
    # question과 코드는 유사. 차이점이라면 답변의 경우 질문에 종속되는 부가적인 정보이므로 질문에 대한 정보 필요.
    question = get_object_or_404(Question, pk=question_id)  # 질문에 대한 정보 가져옴. 없을경우 처리불가(404 에러)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user  # 답변 작성자 정보 등록
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    """ 답변 수정 """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '게시글 관리 권한이 없습니다.')  # request 빼먹어서 오류 뜸
        return redirect('pybo:detail', question_id=answer.question.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pybo:detail', question_id=answer.question.id)
    # else문 들여쓰기 착각으로 인해 20분동안 헤맴
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    """ 답변 삭제 """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '게시글 관리 권한이 없습니다.')
    else:
        answer.delete()
    return redirect('pybo:detail', question_id=answer.question.id)


