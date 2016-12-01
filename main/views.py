from django.shortcuts import render
from .models import CompInv
from .models import System
from .models import PhotoBase
# from django.utils import timezone
import datetime




def inv(request):
    field_name = None
    if request.method == "GET":
        nod_up = request.GET.get('nod_up')
        if nod_up:
            System.get_nod()
        day_all = request.GET.get('day_all')
        if day_all:
            System.Show_Data(day_all)
        field_name = request.GET.get('field_name')
        if field_name:
            System.Sort_Update(field_name)
            Sort_by = System.objects.get(sys_field1=field_name).sys_field4 + field_name
            date_of_view = datetime.datetime.strptime(System.objects.get(desc_name='type_of_view').sys_field5, '%Y-%m-%d')
            table = CompInv.objects.filter(pub_date__gte=date_of_view).order_by(Sort_by)
            if not table.exists():
                table = CompInv.objects.filter(
                    pub_date__date=(datetime.date.today() - datetime.timedelta(days=1))).order_by(Sort_by)
                System.objects.filter(desc_name='type_of_view').update(sys_field1="Yesterday")



    if not field_name:
        System.Sort_Update('zero')
        date_of_view = datetime.datetime.strptime(System.objects.get(desc_name='type_of_view').sys_field5, '%Y-%m-%d')
        table = CompInv.objects.filter(pub_date__gte=date_of_view)
        System.objects.filter(desc_name='type_of_view').update(sys_field1="Today")
        if not table.exists():
            table = CompInv.objects.filter(pub_date__date=(datetime.date.today() - datetime.timedelta(days=1)))
            System.objects.filter(desc_name='type_of_view').update(sys_field1="Yesterday")

    System.Show_Data('day')
    add_to_name = System.objects.filter(desc_name='type_of_view')[0]
    eset_d = System.objects.filter(desc_name="eset_nod_act_v")[0]
    but_arr = System.objects.filter(desc_name="sort_buttons_arrows")
    filters = lambda x: CompInv.objects.values_list(
        x, flat=True).distinct().order_by(x)
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
            System.get_nod()
        field_name = request.GET.get('field_name')

        if field_name:

            svalue = request.GET.get('svalue')
            stype = request.GET.get('stype')
            System.Sort_Update(field_name)
            Sort_by = System.objects.get(sys_field1=field_name).sys_field4 + field_name
            table = CompInv.objects.filter(**{stype: svalue}).filter(
                    pub_date__gte=(datetime.date.today() - datetime.timedelta(days=7))).order_by(Sort_by)
            table_today = CompInv.objects.filter(**{stype: svalue}).latest('pub_date')
            collapse = ''

    if not field_name:
        svalue = svalue
        stype = stype
        collapse = 'in'

        table = CompInv.objects.filter(**{stype: svalue}).filter(
                    pub_date__gte=(datetime.date.today() - datetime.timedelta(days=7)))
        table_today = table.latest('pub_date')

    if PhotoBase.objects.filter(sam_name=svalue).exists() or PhotoBase.objects.filter(sam_name=(table_today.user_name)).exists():
        if stype == 'user_name':
            photo_url = PhotoBase.objects.filter(sam_name=svalue)[0]
        elif stype == 'comp_name':photo_url = PhotoBase.objects.filter(sam_name=(table_today.user_name))[0]
    else:
        photo_url = PhotoBase.objects.filter(sam_name='no_user')[0]
    System.objects.filter(desc_name="type_of_view").update(
        sys_field4='btn-info disabled',
        sys_field3='btn-info disabled')
    add_to_name = System.objects.filter(desc_name='type_of_view')[0]
    eset_d = System.objects.filter(desc_name="eset_nod_act_v")[0]
    but_arr = System.objects.filter(desc_name="sort_buttons_arrows")
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
        'filt_un': filters('user_name')})

