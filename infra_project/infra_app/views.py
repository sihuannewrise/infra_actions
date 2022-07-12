from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Ups, I did it again!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
