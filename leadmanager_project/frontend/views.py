from django.shortcuts import render


def index(request):
    ''' ให้ดูที่ index.html ซึ่งเป็น react templates'''
    return render(request, 'frontend/index.html')
