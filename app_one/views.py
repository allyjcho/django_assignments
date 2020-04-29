from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Placeholder to later list of blogs")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number {number}.")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog{number}.")

def destroy(request, number):
    return redirect('/')