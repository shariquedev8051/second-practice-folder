from datetime import date
from django.shortcuts import redirect, render
from .models import Book
from django.http import HttpResponse
# Create your views here.

import logging
logger = logging.getLogger('newlogger')

def func(request):  # function based view
    return render(request, 'base.html')
    # print(request.method) #? to see the type of request
    # print('----------------In func-------------') #? testing purpose
    # return HttpResponse('Hi welcome to web page')
    # return JsonResponse({'key':'value'})
def testing_log(request):
    for i in range(20):
        logger.debug(f"test no:- {i} started")
        logging.debug("Message from debug")
        logging.info("Message from info")
        logging.warning("Message from warning")
        logging.error("Message from error")
        logging.critical("Message from critical")
        logger.debug(f"test no:- {i} ednded ")
    return HttpResponse("<h1>Hi there</h1>")

def homepage(request):  # we have to return something
    logger.info(f'{request.user}')
    logger.info(f'{request.build_absolute_uri}')
    if request.method == 'POST':
        data = request.POST
        if not data.get("id"):
            if data['ispub'] == 'Yes':
                Book.objects.create(
                    name=data['nm'],
                    qty=data['qty'],
                    price=data['price'],
                    is_published=True,
                    published_date=date.today()
                )
            elif data['ispub'] == 'No':
                Book.objects.create(
                    name=data['nm'],
                    qty=data['qty'],
                    price=data['price'],
                    # is_published=False #? defalut value is false
                    #
                )
            return redirect('home')
        else:
            bid = data.get("id")
            book_obj = Book.objects.get(id= bid)
            book_obj.name = data['nm']
            book_obj.qty = data['qty']
            book_obj.price = data['price']
            if data['ispub'] == 'Yes':
                if book_obj.is_published:
                    pass
                else:
                    book_obj.is_published = True
                    book_obj.published_date = date.today()
            elif data['ispub'] == 'No':
                if book_obj.is_published == True:
                    pass
            book_obj.save()
            return redirect('home')
    else:
        return render(request, template_name='home.html')


def get_books(request):
    """To perfrom CRUDE Read operation"""
    books = Book.objects.all()
    return render(request, template_name='books.html', context={'all_books': books})


def delete_book(request, id):
    """To perform CRUDE Delete operation"""
    # print(id, "delete book id") # debug
    Book.objects.get(id=id).delete()
    return redirect('show books')

def update_book(request ,id):
    """To perform CRUD Update operation"""
    book_obj = Book.objects.get(id = id)
    return render(request, "home.html", context={"single_book":book_obj})
    

def soft_delete(request, id):
    book_obj = Book.objects.get(id = id)
    book_obj.is_deleted = 'Y'
    book_obj.save()
    return redirect('show books')


def active_books(request):
    # all_active_books = Book.objects.filter(is_deleted = 'N')
    all_active_books = Book.active_books.all()
    return render (request , template_name='books.html', context={'all_books': all_active_books})


def inactive_books(request):
    # all_inactive_books = Book.objects.filter(is_deleted = 'Y')
    all_inactive_books = Book.inactive_books.all()
    return render(request, template_name='books.html' , context={"all_books":all_inactive_books,"book_status":"InActive"})