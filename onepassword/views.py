from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from onepassword.utils import getrandompassword

@login_required
def index(request):
    password = getrandompassword()
    return render(
        request, 'onepssword/index.html',
        {'randompassword': password}
    )

@login_required
def generaterandompassword(request):
    if request.method == 'GET':
        is_numbers = request.GET.get('is_numbers', 'true')
        is_symbols = request.GET.get('is_symbols', 'false')
        length = int(request.GET.get('length', 8))
        _type = request.GET.get('type', 'characters')
        password = getrandompassword(is_numbers, is_symbols, length, _type)
        return JsonResponse({'randompassword': password})
