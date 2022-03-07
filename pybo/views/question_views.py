from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    """ pybo 질문 등록 """
    # 질문 등록의 경우 get인 경우 질문 작성 양식만 가져오고, post인 경우 데이터가 저장되어야 하므로 각각에 대한 처리.
    if request.method == 'POST':  # 웹 페이지 요청 방식이 post인 경우 화면에서 전달받은 데이터로 양식 값이 채워지도록 설정.
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # 임시 저장 아님
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:  # else로 걸러지는 대부분의 요청방식은 get일 것이고, 이 경우 입력값 없이 객체 생성.
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """ 게시글 수정 """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '게시글 관리 권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)  # 기존에 저장된 제목, 내용이 반영된 작성 양식 불러오기 위해 instance 설정
        if form.is_valid():
            question = form.save(commit=False)  # 임시 저장 아님
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('pybo:detail', question_id=question.id)
    else:  # else로 걸러지는 대부분의 요청방식은 get일 것이고, 이 경우 입력값 없이 객체 생성.
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """ 게시글 삭제 """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '게시글 관리 권한이 없습니다.')
        return redirect('pybo:detail', question_id=question.id)
    question.delete()
    return redirect('pybo:index')
