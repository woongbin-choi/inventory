from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from ..forms import TakeoutForm
from ..models import Takeout

@login_required(login_url='common:login')
def takeout_create(request):
    """
    반출 물질 등록
    """
    if request.method == 'POST':
        form = TakeoutForm(request.POST)
        if form.is_valid():
            takeout = form.save(commit=False)
            takeout.author = request.user
            takeout.save()
            return redirect('control:indexB')
    else:
        form = TakeoutForm()
    context = {'form': form}
    return render(request, 'control/takeout_form.html', context)

@login_required(login_url='common:login')
def takeout_modify(request, takeout_id):
    """
    반출 물질 수정
    """
    takeout = get_object_or_404(Takeout, pk=takeout_id)
    if request.user != takeout.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('control:detail', takeout_id=takeout.id)

    if request.method == "POST":
        form = TakeoutForm(request.POST, instance=takeout)
        if form.is_valid():
            takeout = form.save(commit=False)
            takeout.author = request.user
            takeout.save()
            return redirect('control:detail', takeout_id=takeout.id)
    else:
        form = TakeoutForm(instance=takeout)
    context = {'form': form}
    return render(request, 'control/takeout_form.html', context)

@login_required(login_url='common:login')
def takeout_delete(request, takeout_id):
    """
    반출 물질 삭제
    """
    takeout = get_object_or_404(Takeout, pk=takeout_id)
    if request.user != takeout.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('control:detail', takeout_id=takeout.id)
    takeout.delete()

    return redirect('control:indexB')