from django.shortcuts import render, HttpResponse


def index(request):
    ''' ให้ดูที่ templates/frontend/index.html จะมีไฟล์หลังจาก build file'''
    return render(request, 'frontend/index.html')
