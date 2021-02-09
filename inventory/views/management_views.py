from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import ManagementForm
from ..models import Management

@login_required(login_url='common:login')
def management_create(request):
    """
    제품등록
    """
    if request.method == 'POST':
        form = ManagementForm(request.POST)
        if form.is_valid():
            management = form.save(commit=False)
            management.save()
            return redirect('inventory:index')
    else:
        form = ManagementForm()
    context = {'form': form}
    return render(request, 'inventory/management_form.html', context)

@login_required(login_url='common:login')
def management_modify(request, management_id):
    """
    제품수정
    """
    management = get_object_or_404(Management, pk=management_id)
    if request.user != management.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('inventory:detail', management_id=management.id)

    if request.method == "POST":
        form = ManagementForm(request.POST, instance=management)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('inventory:detail', management_id=management.id)
    else:
        form = ManagementForm(instance=management)
    context = {'form': form}
    return render(request, 'inventory/management_form.html', context)

@login_required(login_url='common:login')
def management_delete(request, management_id):
    """
    제품삭제
    """
    management = get_object_or_404(Management, pk=management_id)
    if request.user != management.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('inventory:detail', management_id=management.id)
    management.delete()
    return redirect('inventory:index')