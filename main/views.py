from django.shortcuts import render
from main.models import CompInv
from main.models import System_var
from main.models import PhotoBase

import datetime

def inv(request):
    field_name = None
    if request.method == "GET":
        nod_up = request.GET.get('nod_up')
        if nod_up:
            System_var.get_nod()
        day_all = request.GET.get('day_all')
        if day_all:
            System_var.Show_Data(day_all)
        field_name = request.GET.get('field_name')
        if field_name:
            System_var.Sort_Update(field_name)
            Sort_by = [System_var.objects.get(sys_field1=field_name).sys_field4 + field_name]
            date_of_view = datetime.datetime.strptime(System_var.objects.get(desc_name='type_of_view').sys_field5, '%Y-%m-%d')

    if not field_name:
        System_var.Sort_Update('zero')
        date_of_view = datetime.datetime.strptime(System_var.objects.filter(desc_name='type_of_view').first().sys_field5, '%Y-%m-%d')
        Sort_by =[]



    eset_d = System_var.objects.filter(desc_name="eset_nod_act_v").first()
    but_arr = System_var.objects.filter(desc_name="sort_buttons_arrows")
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    if System_var.objects.get(desc_name="type_of_view").sys_field3 == System_var.objects.get(desc_name="type_of_view").sys_field4:
        System_var.Show_Data('day')
    add_to_name = System_var.objects.filter(desc_name='type_of_view').first()
    table = CompInv.objects.filter(pub_date__gte=date_of_view).order_by(*Sort_by)
    return render(request, 'main/sort_n.html', {
        'table': table,
        'but_arr': but_arr,
        'add_to_name': add_to_name,
        'eset_d': eset_d,
        'filt_cn': filters('comp_name'),
        'filt_un': filters('user_name')})

def sort_n(request, svalue, stype):
    field_name = None
    if request.method == "GET":
        nod_up = request.GET.get('nod_up')
        if nod_up:
            System_var.get_nod()
        field_name = request.GET.get('field_name')

        if field_name:
            svalue = svalue
            stype = stype
            System_var.Sort_Update(field_name)
            Sort_by = [System_var.objects.get(sys_field1=field_name).sys_field4 + field_name]
            collapse = ''

    if not field_name:
        System_var.Show_Data('day')
        System_var.Sort_Update('zero')
        svalue = svalue
        stype = stype
        collapse = 'in'
        Sort_by=[]


    table = CompInv.objects.filter(**{stype: svalue}).order_by(*Sort_by)
    table_today = CompInv.objects.filter(**{stype: svalue}).latest('pub_date')

    if PhotoBase.objects.filter(sam_name=svalue).exists() or PhotoBase.objects.filter(sam_name=(table_today.user_name)).exists():
        if stype == 'user_name':
            photo_url = PhotoBase.objects.filter(sam_name=svalue)[0]
        elif stype == 'comp_name':photo_url = PhotoBase.objects.filter(sam_name=(table_today.user_name))[0]
    else:
        photo_url = PhotoBase.objects.filter(sam_name='no_user')[0]
    System_var.objects.filter(desc_name="type_of_view").update(
        sys_field4='btn-info disabled',
        sys_field3='btn-info disabled')
    add_to_name = System_var.objects.filter(desc_name='type_of_view')[0]
    eset_d = System_var.objects.filter(desc_name="eset_nod_act_v")[0]
    but_arr = System_var.objects.filter(desc_name="sort_buttons_arrows")
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)




    return render(request, 'main/inv3.html', {
        'table': table,
        'svalue': svalue,
        'stype' : stype,
        'collapse': collapse,
        'add_to_name': add_to_name,
        'table_today': table_today,
        'but_arr': but_arr,
        'eset_d': eset_d,
        'photo_url': photo_url,
        'filt_cn': filters('comp_name'),
        'filt_un': filters('user_name')
     })

