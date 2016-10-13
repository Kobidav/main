from django.shortcuts import render
from .models import Post
from .models import CompInv
from django.utils import timezone
import datetime


def units(request):
    all_units = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/units.html', {'all_units': all_units})


def inv(request):
    global last_sort
    last_sort = ""
    Name = "All"
    add_to_name = "Main page"
    ftype = "sort"
    table = CompInv.objects.filter(pub_date__date=datetime.date.today())
    return render(request, 'main/inv.html', {
        'table': table, 'add_to_name': add_to_name, 'name': Name, 'ftype': ftype})


def inv3(request, ffname, fvalue):
    # pk_item = pk
    # Name = (CompInv.objects.get(pk=pk_item).comp_name)
    # Name = pk[0:-2] + "-" + pk[-2:]
    Name = fvalue
    ftype = ffname
    add_to_name = "Filtring by " + fvalue
    table = CompInv.objects.filter(**{ftype: Name})
    table_today = CompInv.objects.filter(**{
        ftype: Name}).filter(pub_date__date=datetime.date.today())
    return render(request, 'main/inv3.html', {
        'table': table, 'name': Name, 'add_to_name': add_to_name, 'ftype': ftype, 'table_today': table_today})


# def inv3(request, pk):
#     Name = pk
#     table = CompInv.objects.filter(user_name__contains=Name)
#     # table = CompInv.objects.all()
#     return render(request, 'main/inv3.html', {'table': table, 'name': Name})


def sort_n(request, fsname, svalue, stype):
    add_to_name = "Sorting"
    ftype = stype
    Name = svalue
    sSort = last_sort + fsname
    if Name == "All":
        table = CompInv.objects.filter(pub_date__date=datetime.date.today()).order_by(sSort)
    else:
        table = CompInv.objects.filter(**{ftype: Name}).order_by(sSort)
        table_today = CompInv.objects.filter(**{
        ftype: Name}).filter(pub_date__date=datetime.date.today())
        if last_sort == "":
            global last_sort
            last_sort = "-"
        elif last_sort == "-":
            global last_sort
            last_sort = ""
        return render(request, 'main/inv3.html', {
        'table': table, 'name': Name, 'add_to_name': add_to_name, 'ftype': ftype, 'table_today': table_today})

    if last_sort == "":
        global last_sort
        last_sort = "-"
    elif last_sort == "-":
        global last_sort
        last_sort = ""
    return render(request, 'main/sort_n.html', {
        'table': table, 'name': Name, 'add_to_name': add_to_name, 'ftype': ftype})
