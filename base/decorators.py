from django.shortcuts import redirect
from django.urls import reverse

<<<<<<< HEAD
=======
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)
        
    return wrapper_func


>>>>>>> 641d81093d2a075d10bcc7484ca20a49d2de8f63
def allowed_users(allowed_roles):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None
<<<<<<< HEAD
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
=======
            if request.users.group.exists():
                group = request.user.group.all()[0].name
>>>>>>> 641d81093d2a075d10bcc7484ca20a49d2de8f63

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
<<<<<<< HEAD
                # redirect the user to a different page based on their role
                if group == 'admin':
                    # redirect to the admin page
                    return redirect(reverse('admin'))
                elif group == 'project cordinator':
                    # redirect to the staff page
                    return redirect('test')
                else:
                    # redirect to the default page
                    return redirect('home')
        return wrapper_func
    return decorator
=======
                return HttpResponse('you are not authorised to acces this page')
        return wrapper_func
    return decorator
        
>>>>>>> 641d81093d2a075d10bcc7484ca20a49d2de8f63
