import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader, Context

from .forms import VisitorForm
from .models import Visitor


def index(request):
    return render(request, 'visitors/index.html')


def new(request):
    form_class = VisitorForm

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save(commit=False)
            visitor.save()
            messages.success(request, 'Thanks for signing in!',
                             extra_tags='alert')
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


def export(request):
    all_visitors = Visitor.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="fd_list.csv"'

    writer = csv.writer(response, csv.excel)

    for v in all_visitors:
        writer.writerow([
            v.first_name,
            v.last_name,
            v.call_sign,
            v.nfarl_member,
            v.contact_me,
            v.email,
            v.first_time,
            v.younger_than_18,
        ])

    return response

#    return render(request, 'visitors/export.html', {
#        'all_visitors': all_visitors,
#    })
