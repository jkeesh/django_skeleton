from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponse

from todo.forms import RegistrationForm

def index(request):
	if request.user.is_authenticated():
		pass
		## Will do something

	form = RegistrationForm()

	return render_to_response("login.html", {
			"form": form,
        },
        context_instance = RequestContext(request)
    )