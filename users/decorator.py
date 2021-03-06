from django.shortcuts import redirect
from .models import Users

def admin_required(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login/')
        user = Users.objects.get(email = user)
        if user.level != 'admin':
            return redirect('/')
        return func(request, *args, **kwargs)
    return wrap