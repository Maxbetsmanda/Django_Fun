# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

  # the index function is called when root is visited
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 1

    context = {"rstring": get_random_string(length=14)}

    return render(request,'random_word/index.html', context)

def process(request):
    request.session['count'] += 1
    return redirect('/')

def reset(request):
    del request.session['count']
    return redirect('/')
