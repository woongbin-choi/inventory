from django.http import HttpResponse

def home(request):
    return HttpResponse("시약/소모품 재고관리")