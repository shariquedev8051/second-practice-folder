from django.shortcuts import render, redirect
from django.http import HttpResponse, response


# Create your views here.

def setcookie(request):
    response = render(request, 'cookie.html')
    if request.COOKIES.get('visits'):
        value = int(request.COOKIES.get('visits'))
        response.set_cookie('visits' ,value+1)
    else:
        value = 1
        text = 'Welcome for the first time'
        response.set_cookie('visits', value)
        response.set_cookie('data',text)
    return response

def homepage(request):
    # print(request.COOKIES.items())
    return HttpResponse("<h1>Hi you are in home</h1>")

def getcookie(request):
    nm = request.COOKIES.get("name")
    ag = request.COOKIES.get("age")
    return render (request, "show_cookie.html")

def delete_cookies(request):
    response = redirect('home')
    response.delete_cookie('name')
    response.delete_cookie('age')
    return response

#--------------------------------Session--------------------------#

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Welcome to Django session</h1>")
    
def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookies deleted")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response

def demo_view(request):
    print(request.session.test_cookie_worked())
    return HttpResponse("In demo view")

def create_session(request):
    print(request.session.__dict__)
    request.session['name'] = 'Sharique'
    request.session['password'] = 'Python'
    request.session['age'] = '25'
    request.session['city'] = 'Amravati'
    print(request.session.__dict__)
    return HttpResponse("<h1>Session is set</h1>")

def show_session_data(request):
    return render(request, 'session.html')

def session_delet(request):
    print(request.session.items())
    del request.session['name']
    del request.session['password']
    del request.session['age']
    return render(request, 'session.html')
