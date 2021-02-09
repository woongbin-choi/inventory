from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from ..models import Management

def index(request):
    """
    제품 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어

    # 조회
    management_list = Management.objects.order_by('-registration_date')
    if kw:
        management_list = management_list.filter(
            Q(product_name__icontains=kw) |  # 제목검색
            Q(storage_location__icontains=kw) | # 보관위치검색
            Q(partname__icontains=kw) # 부서명검색
        ).distinct()
    # 페이징처리
    paginator = Paginator(management_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'management_list': page_obj, 'page': page, 'kw': kw}  # page와 kw가 추가

    return render(request, 'inventory/management_list.html', context)


def detail(request, management_id):
    """
    제품 내용 출력
    """
    management = get_object_or_404(Management, pk=management_id)
    context = {'management': management}

    return render(request, 'inventory/management_detail.html', context)