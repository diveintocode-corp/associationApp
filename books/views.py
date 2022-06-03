from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book
from .forms import BookForm


def index(request):
    books = Book.objects.all()
    params = {
        'books': books,
    }
    return render(request, 'books/index.html', params)


def create(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        book = Book(title=title, content=content)
        book.save()
        return redirect('books:index')
    else:
        params = {
            'form': BookForm(),
        }
        return render(request, 'books/create.html', params)


def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    params = {
        'book': book,
    }
    return render(request, 'books/detail.html', params)


def edit(request, book_id):
    book = Book.objects.get(id=book_id)
    if (request.method == 'POST'):
        book.title = request.POST['title']
        book.content = request.POST['content']
        book.save()
        return redirect('books:detail', book_id)
    else:
        form = BookForm(initial={
            'title': book.title,
            'content': book.content,
        })
        params = {
            'book': book,
            'form': form,
        }
        return render(request, 'books/edit.html', params)


def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    if (request.method == 'POST'):
        book.delete()
        return redirect('books:index')
    else:
        params = {
            'book': book,
        }
        return render(request, 'books/delete.html', params)
