from django.http.response import HttpResponse


def my_middleware(get_respone):
    # one time configurattion and initiation
    print("Configuration...!") # It will initilize once when runserver
    def middleware(request):
        # code to be executed for each request before 
        # the views (and later middleware) is called.
        print('Before calling views')
        response =  get_respone(request)
        print(response.content, 'response')
        print("After calling views")

        # code to be executed for each request/ response
        # after the view is called.

        # return HttpResponse("Bye Bye")
        return response

    return middleware



# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("One-time configuration and initialization.")
#         # One-time configuration and initialization.

#     def __call__(self, request):
#         print("Before calling View")
#         response = self.get_response(request)
#         print("After calling View")
#         return response

class MyMiddleware_A:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One-time configuration and initialization.... A")
        # One-time configuration and initialization.

    def __call__(self, request):
        print("Before calling View -- cw -- A")
        response = self.get_response(request)
        print("After calling View -- cw -- A")
        return response


class MyMiddleware_B:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One-time configuration and initialization.... B")
        # One-time configuration and initialization.

    def __call__(self, request):
        print("Before calling View -- cw -- B")
        res = HttpResponse("<h1>Somethiing Wrong Happenend!!!</h1>")
        # response = self.get_response(request)
        print("After calling View -- cw -- B")
        return res
        return response


class MyMiddleware_C:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One-time configuration and initialization.... C")
        # One-time configuration and initialization.

    def __call__(self, request):
        print("Before calling View -- cw -- C")
        response = self.get_response(request)
        print("After calling View -- cw -- C")
        return response


class HooksMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One-time configuration and initialization.... Hook")
        # One-time configuration and initialization.

    def __call__(self, request):
        print("Before calling View -- cw -- Hook")
        response = self.get_response(request)
        print("After calling View -- cw -- Hook")
        return response

    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print("In process view")
    #     # return HttpResponse(f"You can not call {view_func.__name__} view function.. ") # won't call view function
    #     return None   #Will allow to access the view function 
    
    # def process_exception(self, request, exception):
    #     msg = f'{exception.__class__.__name__}{exception}'
    #     return HttpResponse(msg)
    
    def process_template_response(self, request, response):
        response.context_data['name'] = "Tejaswini"
        print("In Process Template Response")
        return response
