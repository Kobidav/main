from django.shortcuts import render
from .models import CompInv
from .models import System
# from django.utils import timezone
import datetime
from .nod import Eset_version


def inv(request):
    Name = "All"
    add_to_name = "Main page"
    ftype = "sort"
    last_srt = '+'
    srt_f_name = 'comp_name'
    show_data = 'day_only'
    table = CompInv.objects.filter(
        pub_date__date=datetime.date.today()).order_by('comp_name')

    eset_d = Eset_version.data.date()
    eset_v = Eset_version.version
    Eset_version.get()
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    but_arr = System.objects.filter(desc_name="sort_buttons_arrows")

    return render(request, 'main/sort_n.html', {
        'table': table,
        'add_to_name': add_to_name,
        'name': Name,
        'ftype': ftype,
        'eset_d': eset_d,
        'eset_v': eset_v,
        'last_srt': last_srt,
        'srt_f_name': srt_f_name,
        'filt_cn': filters('comp_name'),
        'filt_un': filters('user_name'),
        'show_data': show_data,
        'but_arr': but_arr})


def inv3(request, ffname, fvalue):
    Name = fvalue
    ftype = ffname
    last_srt = "+"
    show_data = 'day_only'
    add_to_name = "Filtring by "
    but_arr = System.objects.filter(desc_name="sort_buttons_arrows")
    table = CompInv.objects.filter(**{ftype: Name}).order_by('-pub_date')[0:3]
    table_today = CompInv.objects.filter(
        **{ftype: Name}).filter(pub_date__date=datetime.date.today())
    eset_d = Eset_version.data.date()
    eset_v = Eset_version.version
    return render(request, 'main/inv3.html', {
        'table': table,
        'name': Name,
        'last_srt': last_srt,
        'add_to_name': add_to_name,
        'ftype': ftype,
        'table_today': table_today,
        'but_arr': but_arr,
        'show_data': show_data,
        'eset_d': eset_d,
        'eset_v': eset_v})


def sort_n(request, fsname, svalue, stype, lst_srt, shw_data):
    add_to_name = "Sorting"
    ftype = stype
    Name = svalue
    last_sort = lst_srt
    if last_sort == '+':
        last_sort = ''
    sSort = last_sort + fsname
    srt_f_name = fsname
    show_data = shw_data
    if show_data == "day_only":
        var_show_data = datetime.date.today()
    elif show_data == "all_database":
        var_show_data = datetime.date(2016, 10, 19)

    but_arr = System.objects.filter(desc_name="sort_buttons_arrows")
    eset_d = Eset_version.data.date()
    eset_v = Eset_version.version
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    if Name == "All":
        table = CompInv.objects.filter(
            pub_date__gte=var_show_data).order_by(sSort)
    elif Name == "warr":
        table = CompInv.objects.exclude(
            upd_need=0).filter(
            pub_date__gte=var_show_data) | CompInv.objects.exclude(
            eset_nod__gte=14360).filter(
            pub_date__gte=var_show_data).order_by(sSort)
    else:
        table = CompInv.objects.filter(**{ftype: Name}).order_by(sSort)[0:3]
        table_today = CompInv.objects.filter(**{
            ftype: Name}).filter(pub_date__date=datetime.date.today())
        if last_sort == "":
            last_sort = "-"
        elif last_sort == "-":
            last_sort = "+"
        return render(request, 'main/inv3.html', {
            'table': table,
            'name': Name,
            'add_to_name': add_to_name,
            'ftype': ftype,
            'table_today': table_today,
            'but_arr': but_arr,
            'srt_f_name': srt_f_name,
            'show_data': show_data,
            'eset_d': eset_d,
            'eset_v': eset_v,
            'last_srt': last_sort})

    if last_sort == "":
        last_sort = "-"
    elif last_sort == "-":
        last_sort = "+"
    return render(request, 'main/sort_n.html', {
        'table': table,
        'name': Name,
        'add_to_name': add_to_name,
        'ftype': ftype,
        'eset_d': eset_d,
        'eset_v': eset_v,
        'last_srt': last_sort,
        'srt_f_name': srt_f_name,
        'but_arr': but_arr,
        'show_data': show_data,
        'filt_cn': filters('comp_name'),
        'filt_un': filters('user_name')})


def warr(request):
    last_sort = "+"
    Name = "warr"
    add_to_name = "Wranings"
    ftype = "sort"
    srt_f_name = 'comp_name'
    but_arr = System.objects.filter(desc_name="sort_buttons_arrows")
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    table = CompInv.objects.exclude(
        upd_need=0).filter(
        pub_date__date=datetime.date.today()) | CompInv.objects.exclude(
        eset_nod__gte=14360).filter(
        pub_date__date=datetime.date.today())
    Eset_version.get()
    eset_d = Eset_version.data.date()
    eset_v = Eset_version.version
    return render(request, 'main/sort_n.html', {
        'table': table,
        'add_to_name': add_to_name,
        'name': Name,
        'ftype': ftype,
        'srt_f_name': srt_f_name,
        'last_srt': last_sort,
        'eset_d': eset_d,
        'eset_v': eset_v,
        'but_arr': but_arr,
        'filt_cn': filters('comp_name'),
        'filt_un': filters('user_name')})
