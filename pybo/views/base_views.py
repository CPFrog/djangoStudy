from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


def index(request):
    """ pybo 목록 출력 """
    page = request.GET.get('page', '1')  # 최초 페이지 번호

    question_list = Question.objects.order_by('-create_date')  # 최근 작성일 순으로 게시글 정렬하기 위해 - 붙임

    # 게시판 페이징 처리
    paginator = Paginator(question_list, 10)  # 10개 단위로 페이지 나누기 위한 코드
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}  # 게시글들 목록이 담긴 리스트
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """ pybo 내용 출력 """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
