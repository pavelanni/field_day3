from django.shortcuts import render, HttpResponse, redirect
from django.template import loader

from .forms import VisitorForm
from .models import Visitor

def index(request):
    return HttpResponse("Hello, world! Here is the first Visitors page.")

def new(request):
    form_class = VisitorForm

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.save()
            return redirect('new')
    else:
        visitor_number = len(Visitor.objects.all()) + 1
        form = VisitorForm()

    return render(request, 'visitors/new.html', {
        'form': form_class,
        'visitor_number': visitor_number,
    })

def list(request):
    all_visitors = Visitor.objects.all()

    return render(request, 'visitors/list.html', {
        'all_visitors': all_visitors,
    })
