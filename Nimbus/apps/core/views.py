import logging
from .forms import AuthenticateForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic.base import View


logger = logging.getLogger(__name__)


def index(request, auth_form=None):
    if request.user.is_authenticated():
        print (request.user)
        return dashboard_view(request)
    else:
        auth_form = auth_form or AuthenticateForm()
        request.session.set_test_cookie()
        return render(request, "core/login.html", {
            "auth_form": auth_form
        })


class login_view(View):
    def post(self, request):
        form = AuthenticateForm(data=request.POST)
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        else:
            logger.error("No cookie support detected! This could cause problems.")
        if form.is_valid():
            login(request, form.get_user())
            logger.info("Login succeeded as {}".format(request.POST.get("username", "unknown")))
            next = request.GET.get("next", "/")
            return redirect(next)
        else:
            logger.info("Login failed as {}".format(request.POST.get("username", "unknown")))
            return index(request, auth_form=form)  # Modified to show errors


def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def dashboard_view(request):
    return render(request, "core/dashboard.html", {

    })
