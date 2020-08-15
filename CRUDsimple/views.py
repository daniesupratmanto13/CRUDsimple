from django.shortcuts import render


def index(request):

    context = {
        'title': 'CRUDsimple',
        'title_content': 'Love Book',
    }

    return render(request, 'index.html', context)
