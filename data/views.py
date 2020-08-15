from django.shortcuts import render, redirect
from .forms import BookForm
from .models import BookModel

# Create your views here.


def index(request):

    book_all = BookModel.objects.all()
    book_form = BookForm(request.POST or None)
    if request.method == 'POST':
        if book_form.is_valid:
            book_form.save()

    context = {
        'title': 'Library | CRUDsimple',
        'title_content': 'Book Data',
        'book_all': book_all,
        'book_form': book_form,
    }

    return render(request, 'data/index.html', context)


def update(request, idInput):

    list_id = BookModel.objects.values_list('id')
    list_id = sorted(list_id)
    listId = []
    for l in list_id:
        listId.append(l[0])

    idInput1 = listId[:listId.index(idInput)]
    idInput2 = listId[(listId.index(idInput)+1):]

    books1 = BookModel.objects.filter(pk__in=idInput1)
    books2 = BookModel.objects.filter(pk__in=idInput2)
    book = BookModel.objects.get(id=idInput)

    data = {
        'genre': book.author,
        'title': book.title,
        'genre': book.genre,
    }

    form = BookForm(
        request.POST or None,
        initial=data,
        instance=book,
    )

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('data:index')

    context = {
        'title': 'Update | CRUDsimple',
        'title_content': 'Update Book Data',
        'books1': books1,
        'books2': books2,
        'form': form,
    }

    return render(request, 'data/update.html', context)


def delete(request, idInput):
    book = BookModel.objects.get(id=idInput).delete()
    return redirect('data:index')
