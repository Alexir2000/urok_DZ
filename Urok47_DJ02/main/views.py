from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def func_index(request):
    data = {
        'caption': 'Шаблоны Django',
    }
    return render(request, 'main/index.html', data)
def func_new(request):
    return render(request, 'main/new.html')

def func_data(request):
    return render(request, 'main/data.html')
def func_test(request):
    return render(request, 'main/test.html')
