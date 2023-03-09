from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!', status=200)


def second_page(request):
    return HttpResponse('А это вторая страница', status=200)
