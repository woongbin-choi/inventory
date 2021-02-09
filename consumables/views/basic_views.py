from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q

def indexA(request):
    """
    소모품 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    question_list = Question.objects.order_by('-item_code')
    if kw:
        question_list = question_list.filter(
            Q(item_code__icontains=kw) |
            Q(product_name__icontains=kw) |
            Q(team_name__icontains=kw)
        ).distinct()
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw}

    return render(request, 'consumables/question_list.html', context)


def detail(request, question_id):
    """
    소모품 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}

    return render(request, 'consumables/question_detail.html', context)