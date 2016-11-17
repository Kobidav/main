from django.shortcuts import render
from .models import CompInv
from .models import System
from .models import PhotoBase
# from django.utils import timezone
import datetime


def plus(last_sort):
    if last_sort == "":
        return "-"
    elif last_sort == "-":
        return "+"


def inv(request):
    Name = "All"
    add_to_name = "Main page today"
    ftype = "sort"
    last_srt = '+'
    srt_f_name = 'comp_name'
    show_data = 'day_only'
    table = CompInv.objects.filter(
        pub_date__date=datetime.date.today()).order_by('comp_name')
    if not table.exists():
        table = CompInv.objects.filter(
            pub_date__date=(datetime.date.today() - datetime.timedelta(
                days=1))).order_by(
            'comp_name')
        add_to_name = "Main page yesterday"

    System.get_nod()
    eset_d = System.objects.filter(desc_name="eset_nod_act_v")[0]
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    but_arr = System.objects.filter(desc_name="sort_buttons_arrows")

    return render(request, 'main/sort_n.html', {
        'table': table,
        'add_to_name': add_to_name,
        'name': Name,
        'ftype': ftype,
        'eset_d': eset_d,
        'last_srt': last_srt,
        'srt_f_name': srt_f_name,
        'filt_cn': filters('comp_name'),
        'filt_un': filters('user_name'),
        'show_data': show_data,
        'but_arr': but_arr})


def sort_n(request, fsname, svalue, stype, lst_srt, shw_data):
    add_to_name = "Sorting"
    if request.method == "GET":
        key = request.GET.get('key')
        #add_to_name = key

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
    System.get_nod()
    eset_d = System.objects.filter(desc_name="eset_nod_act_v")[0]
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    if Name == "All":
        table = CompInv.objects.filter(
            pub_date__gte=var_show_data).order_by(sSort)
    elif Name == "warr":
        add_to_name = "Wranings"
        table = CompInv.objects.exclude(
            upd_need=0).filter(
            pub_date__gte=var_show_data) | CompInv.objects.exclude(
            eset_nod__gte=eset_d.sys_field6).filter(
            pub_date__gte=var_show_data).order_by(sSort)
    else:
        table = CompInv.objects.filter(**{ftype: Name}).order_by(sSort)
        table_today = CompInv.objects.filter(**{
            ftype: Name}).latest('pub_date')
        last_sort = plus(last_sort)
        if PhotoBase.objects.filter(
            sam_name=Name).exists() or PhotoBase.objects.filter(
                sam_name=(table_today.user_name)).exists():
            if ftype == 'user_name':
                photo_url = PhotoBase.objects.filter(sam_name=Name)[0]
            elif ftype == 'comp_name':
                photo_url = PhotoBase.objects.filter(
                    sam_name=(table_today.user_name))[0]
        else:
            photo_url = PhotoBase.objects.filter(sam_name='no_user')[0]

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
            'photo_url': photo_url,
            'last_srt': last_sort,
            'filt_cn': filters('comp_name'),
            'filt_un': filters('user_name')})

    last_sort = plus(last_sort)
    return render(request, 'main/sort_n.html', {
        'table': table,
        'name': Name,
        'add_to_name': add_to_name,
        'ftype': ftype,
        'eset_d': eset_d,
        'last_srt': last_sort,
        'srt_f_name': srt_f_name,
        'but_arr': but_arr,
        'show_data': show_data,
        'filt_cn': filters('comp_name'),
        'filt_un': filters('user_name')})
