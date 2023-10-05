from django.shortcuts import redirect, reverse
from django.conf import settings

def allowed_users(allowed_roles):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            
            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                # redirect the user to the corresponding URL based on their group
                return redirect(reverse(settings.REDIRECT_URLS.get(group, settings.DEFAULT_GROUP)))
        return wrapper_func
    return decorator
