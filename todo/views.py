from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import auth
from django.http import HttpResponse

def index(request):
    return render_to_response("login.html", {

        },
        context_instance = RequestContext(request)
    )