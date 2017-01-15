from django.shortcuts import render, redirect
from main.models import CompInv
from main.models import System_var
from main.models import PhotoBase

import datetime

def hw_drop_list():


    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)

    but_arr_hw = System_var.objects.filter(desc_name="sort_buttons_arrows_hw")
    drop_list_of_hw = []
    for a in but_arr_hw:
        unit_id_dic = {}
        for b in filters(a.sys_field1):
            id_key = CompInv.objects.filter(**{a.sys_field1: b}).latest('pub_date').id
            unit_id_dic[b] = id_key
        drop_list_of_hw.append([a.sys_field1, a.sys_field2, (filters(a.sys_field1)), unit_id_dic])
    return drop_list_of_hw
def hw_tooltip(table):
    if type(table) is list:
        comp_list =[]
        for units in table:
            comp_list.append(units.comp_name)
    else:
        comp_list=table.values_list("comp_name",flat=True)
    list_of_hw_tooltip=[]
    for comp in comp_list:
        string_data = CompInv.objects.filter(comp_name=comp).latest('pub_date')
        unit_of_list = " || ".join([
            string_data.model_name,
            string_data.processor,
            string_data.memory,
            string_data.service_tag])
        list_of_hw_tooltip.append(unit_of_list)
    table = zip(table, list_of_hw_tooltip)
    list_of_hw_tooltip=[]
    for a,b in table:
        list_of_hw_tooltip.append([a,b])
    return list_of_hw_tooltip


def inv(request):
    field_name = None
    main_page = None
    but_arr_hw = None
    date_of_view = None
    Sort_by = []
    if request.method == "GET":
        nod_up = request.GET.get('nod_up')
        if nod_up:
            System_var.get_nod()
        main_page = request.GET.get('inv')
        if main_page:
            System_var.Show_Data('today')
            return redirect('/inv')
        day_all = request.GET.get('day_all')
        if day_all:
            System_var.Show_Data(day_all)
        field_name = request.GET.get('field_name')
        if field_name:
            System_var.Sort_Update(field_name)
            Sort_by = [System_var.objects.filter(desc_name='sort_buttons_arrows').get(sys_field1=field_name).sys_field4 + field_name]

    else:
        System_var.Show_Data('today')
        System_var.Sort_Update('zero')

    if System_var.objects.filter(desc_name='type_of_view'):
        date_of_view = datetime.datetime.strptime(System_var.objects.filter(desc_name='type_of_view').first().sys_field5,
                                              '%Y-%m-%d')
    else:
        System_var.Show_Data('today')
        date_of_view = datetime.datetime.strptime(
            System_var.objects.filter(desc_name='type_of_view').first().sys_field5,
            '%Y-%m-%d')

    if System_var.objects.filter(desc_name="eset_nod_act_v"):
        eset_d = System_var.objects.filter(desc_name="eset_nod_act_v").first()
    else:
        System_var.get_nod()
        eset_d = System_var.objects.filter(desc_name="eset_nod_act_v").first()
    but_arr = System_var.objects.filter(desc_name="sort_buttons_arrows")
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    if System_var.objects.get(desc_name="type_of_view").sys_field3 == System_var.objects.get(desc_name="type_of_view").sys_field4:
        System_var.Show_Data('day')
    add_to_name = System_var.objects.filter(desc_name='type_of_view').first()
    table = CompInv.objects.filter(pub_date__gte=date_of_view).order_by(*Sort_by)
    if System_var.objects.filter(desc_name="sort_buttons_arrows_hw"):
        but_arr_hw = System_var.objects.filter(desc_name="sort_buttons_arrows_hw")
    else:
        System_var.Create_hw_tables()
    drop_list_of_hw = hw_drop_list()
    table = hw_tooltip(table)


    table_today = CompInv.objects.last()
    return render(request, 'main/sort_n.html', {
        'table': table,
        'table_today': table_today,
        'but_arr_hw': but_arr_hw,
        'but_arr': but_arr,
        'add_to_name': add_to_name,
        'eset_d': eset_d,
        'filt_un': filters('user_name'),
        'drop_list_of_hw': drop_list_of_hw
    })

def sort_n(request, svalue, stype):
    field_name = None
    Sort_by = []
    if request.method == "GET":
        main_page = request.GET.get('inv')
        if main_page:
            System_var.Show_Data('today')
            return redirect('/inv')
        nod_up = request.GET.get('nod_up')
        if nod_up:
            System_var.get_nod()
        field_name = request.GET.get('field_name')
        if field_name:
            System_var.Sort_Update(field_name)
            Sort_by = [System_var.objects.filter(desc_name='sort_buttons_arrows').get(sys_field1=field_name).sys_field4 + field_name]
            collapse = ''

    if not field_name:
        System_var.Show_Data('day')
        System_var.Sort_Update('zero')
        collapse = 'in'

    svalue = svalue
    stype = stype
    disable_button = 'disabled'
    list_of_showing_data = list(CompInv.objects.filter(**{stype: svalue}).order_by('-pub_date').values_list('pub_date',flat=True)[0:8])
    table = CompInv.objects.filter(**{stype: svalue}).filter(pub_date__in=list_of_showing_data).order_by(*Sort_by)
    table_today = CompInv.objects.filter(**{stype: svalue}).latest('pub_date')

    if PhotoBase.objects.filter(sam_name=svalue).exists() or PhotoBase.objects.filter(sam_name=(table_today.user_name)).exists():
        if stype == 'user_name':
            photo_url = PhotoBase.objects.filter(sam_name=svalue)[0]
        elif stype == 'comp_name':photo_url = PhotoBase.objects.filter(sam_name=(table_today.user_name))[0]
    else:
        photo_url = PhotoBase.objects.filter(sam_name='no_user')[0]
    add_to_name = System_var.objects.filter(desc_name='type_of_view')[0]
    eset_d = System_var.objects.filter(desc_name="eset_nod_act_v")[0]
    but_arr = System_var.objects.filter(desc_name="sort_buttons_arrows")
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    but_arr_hw = System_var.objects.filter(desc_name="sort_buttons_arrows_hw")
    drop_list_of_hw = hw_drop_list()
    table = hw_tooltip(table)


    return render(request, 'main/sort_n.html', {
        'table': table,
        'svalue': svalue,
        'stype' : stype,
        'collapse': collapse,
        'add_to_name': add_to_name,
        'table_today': table_today,
        'but_arr': but_arr,
        'eset_d': eset_d,
        'photo_url': photo_url,
        'filt_un': filters('user_name'),
        'disable_button': disable_button,
        'drop_list_of_hw': drop_list_of_hw
     })

def hard(request, hwtype, hwvalue):
    Sort_by =[]
    field_name = None
    if request.method == "GET":
        main_page = request.GET.get('inv')
        if main_page:
            System_var.Show_Data('today')
            return redirect('/inv')
        nod_up = request.GET.get('nod_up')
        if nod_up:
            System_var.get_nod()
        day_all = request.GET.get('day_all')
        if day_all:
            System_var.Show_Data(day_all)
        field_name = request.GET.get('field_name')
        if field_name == 'comp_name':
            System_var.Sort_Update(field_name)
            Sort_by = [System_var.objects.filter(desc_name='sort_buttons_arrows').get(sys_field1=field_name).sys_field4 + field_name]
        else:
            System_var.Sort_Update('zero')
            Sort_by = []
    if not field_name:
        System_var.Sort_Update('zero')
        Sort_by = []


    hwtype = hwtype
    hw_id=hwvalue
    hwvalue = CompInv.objects.filter(id=hw_id).values_list(hwtype,flat=True).last()
    disable_button = 'disabled'

    if hasattr(CompInv.objects.filter(**{hwtype: hwvalue}),"__iter__"):
        g = CompInv.objects.filter(**{hwtype: hwvalue}).values_list('comp_name',flat=True).distinct().order_by(*Sort_by)
        c = []
        for a in g:
            b = CompInv.objects.filter(comp_name= a).latest('pub_date')
            c.append(b)
        table = c

    else:
        table = CompInv.objects.filter(**{hwtype: hwvalue}).order_by('-pub_date')
    table_today=CompInv.objects.filter(**{hwtype: hwvalue}).latest('pub_date')
    add_to_name = System_var.objects.filter(desc_name='type_of_view')[0]
    eset_d = System_var.objects.filter(desc_name="eset_nod_act_v")[0]
    but_arr = System_var.objects.filter(desc_name="sort_buttons_arrows")
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
    but_arr_hw = System_var.objects.filter(desc_name="sort_buttons_arrows_hw")
    drop_list_of_hw = hw_drop_list()
    table = hw_tooltip(table)

    return render(request, 'main/sort_n.html', {
        'table': table,
        'add_to_name': add_to_name,
        'but_arr_hw': but_arr_hw,
        'table_today': table_today,
        'but_arr': but_arr,
        'eset_d': eset_d,
        'filt_un': filters('user_name'),
        'disable_button' : disable_button,
        'drop_list_of_hw': drop_list_of_hw
    })