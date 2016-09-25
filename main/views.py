from django.shortcuts import render
from .models import Post
from .models import CompInv
from django.utils import timezone
from django_tables2 import RequestConfig
from .tables import PersonTable
from .tables import PersonTable2


def units(request):
    all_units = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/units.html', {'all_units': all_units})


def people(request):
    table2 = PersonTable(CompInv.objects.filter(
        user_name__contains='Administrator').order_by('user_name'))
    RequestConfig(request).configure(table2)
    return render(request, 'main/people.html', {'table2': table2})


def inv(request):

    # table = PersonTable2(CompInv.objects.order_by('CompName').distinct())
    #table = PersonTable2(CompInv.objects.all())
    # RequestConfig(request).configure(table)
    #table = CompInv.objects.filter(user_name__contains='Administrator').order_by('user_name')
    return render(request, 'main/inv.html', {'table': table})
