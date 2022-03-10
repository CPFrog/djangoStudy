from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question


def index(request):
    """ pybo 목록 출력 """
    page = request.GET.get('page', '1')  # 페이지 번호. 최초 번호=1
    kw = request.GET.get('kw', '')  # 검색어, 디폴트 검색어=''

    question_list = Question.objects.order_by('-create_date')  # 최근 작성일 순으로 게시글 정렬하기 위해 - 붙임
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목으로 검색
            Q(content__icontains=kw) |  # 내용으로 검색
            Q(author__username=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()

    # 게시판 페이징 처리
    paginator = Paginator(question_list, 10)  # 10개 단위로 페이지 나누기 위한 코드
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}  # 게시글들 목록이 담긴 리스트, #3-15 이후 page와 kw 추가
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """ pybo 내용 출력 """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
