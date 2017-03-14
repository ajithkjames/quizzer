from functools import wraps
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View

def requires_teacher_login(f):
    """ Decorator for candidate logins """
    @wraps(f)
    def decorated(request, *args, **kwargs):
        if request.user.profile.account_type != 1:
            return render(request, 'access_check.html')
        return f(request, *args, **kwargs)
    return decorated
class ProtectedTeacherView(View):

    @method_decorator(login_required(login_url='/'))
    @method_decorator(requires_teacher_login)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedTeacherView, self).dispatch(*args, **kwargs)