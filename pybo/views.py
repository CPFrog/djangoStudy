from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator


def index(request):
    """
    pybo 목록 출력
    """
    page = request.GET.get('page', '1')  # 최초 페이지 번호

    question_list = Question.objects.order_by('-create_date')  # 최근 작성일 순으로 게시글 정렬

    # 게시판 페이징 처리
    paginator = Paginator(question_list, 10)  # 10개 단위로 페이지 나누기 위한 코드
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}  # 게시글들 목록이 담긴 리스트
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    """pybo 질문 등록"""
    # 질문 등록의 경우 get인 경우 질문 작성 양식만 가져오고, post인 경우 데이터가 저장되어야 하므로 각각에 대한 처리.
    if request.method == 'POST':  # 웹 페이지 요청 방식이 post인 경우 화면에서 전달받은 데이터로 양식 값이 채워지도록 설정.
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # 임시 저장 아님
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:  # else로 걸러지는 대부분의 요청방식은 get일 것이고, 이 경우 입력값 없이 객체 생성.
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    # question과 코드는 유사. 차이점이라면 답변의 경우 질문에 종속되는 부가적인 정보이므로 질문에 대한 정보 필요.
    question = get_object_or_404(Question, pk=question_id)  # 질문에 대한 정보 가져옴. 없을경우 처리불가(404 에러)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
        context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)
