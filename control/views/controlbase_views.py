from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Takeout
from django.db.models import Q

def indexB(request):
    """
    반출 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    takeout_list = Takeout.objects.order_by('-carry_day')
    if kw:
        takeout_list = takeout_list.filter(
            Q(carry_team__icontains=kw) |
            Q(material_name__icontains=kw) |
            Q(author__username__icontains=kw)
        ).distinct()
    # 페이징처리
    paginator = Paginator(takeout_list, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'takeout_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가되었다.

    return render(request, 'control/takeout_list.html', context)

def detail(request, takeout_id):
    """
    반출 내용 출력
    """
    takeout = get_object_or_404(Takeout, pk=takeout_id)
    context = {'takeout': takeout}

    return render(request, 'control/takeout_detail.html', context)