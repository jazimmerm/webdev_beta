from django.shortcuts import redirect, render

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('drview:homepage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_roles_redirect(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            groups = []
            if request.user.groups.exists():
                groups = request.user.groups.all()
            if any(role.name in allowed_roles for role in groups):
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'drview/not_authorized.html')
        return wrapper_func
    return decorator