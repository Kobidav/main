from django.shortcuts import render
from .models import Post
from .models import CompInv
from django.utils import timezone
from django_tables2 import RequestConfig
from .tables import PersonTable
# from .tables import PersonTable2
# from .forms import PostForm


def units(request):
    all_units = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/units.html', {'all_units': all_units})


def people(request):
    table2 = PersonTable(CompInv.objects.filter(
        user_name__contains='Administrator').order_by('user_name'))
    RequestConfig(request).configure(table2)
    return render(request, 'main/people.html', {'table2': table2})


def Clear(request):
    table2 = PersonTable(CompInv.objects.filter(
        user_name__contains='Administrator').order_by('user_name'))
    RequestConfig(request).configure(table2)
    return render(request, 'main/people.html', {'table2': table2})

# def comp_inv(request):
    # form = PostForm()
    # return render(request, 'main/post_edit.html', {'form': form})


def inv(request):

    # table = PersonTable2(CompInv.objects.order_by('CompName').distinct())
    # table = PersonTable2(CompInv.objects.all())
    # RequestConfig(request).configure(table)
    # table =
    # CompInv.objects.filter(user_name__contains='Administrator').order_by('user_name')
    table = CompInv.objects.all()
    return render(request, 'main/inv.html', {'table': table})


def inv2(request, pk):
    pk_item = pk
    Name = (CompInv.objects.get(pk=pk_item).comp_name)
    table = CompInv.objects.filter(comp_name__contains=Name)
    # table = CompInv.objects.all()
    return render(request, 'main/inv.html', {'table': table})


def inv3(request, pk):
    Name = pk

    table = CompInv.objects.filter(user_name__contains=Name)
    # table = CompInv.objects.all()
    return render(request, 'main/inv.html', {'table': table})


def sort(request, pk):
    Name = pk
    table = CompInv.objects.all().order_by(Name)
    #table = new.table.order_by(Name)
    return render(request, 'main/inv.html', {'table': table})




