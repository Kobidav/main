
from django.core.urlresolvers import reverse
from .models import CompInv, System_var, PhotoBase
from django.test import TestCase
import random


import datetime

def Field_to_None(list_in, field):
    for a in list_in:
        a[field] = None
    return list_in

CompInv_dic = Field_to_None(list(CompInv.objects.values()),'id')
System_var_dic = Field_to_None(list(System_var.objects.values()),'id')
PhotoBase_dic = Field_to_None(list(PhotoBase.objects.values()),'url_name')
Sort_button_names=('comp_name','user_name','date_boot','upd_need','eset_nod','pub_date')





class MainPageTests(TestCase):

    def test_inv_variables_validation(self):
        def Get_site(site, **kwargs):

            response = self.client.get(reverse(site), kwargs)
            return response
        for l in CompInv_dic:
            m = CompInv.objects.create(**l)
            m.save()
        for l in System_var_dic:
            m = System_var.objects.create(**l)
            m.save()
        for l in PhotoBase_dic:
            m = PhotoBase.objects.create(**l)

            m.save()
        if CompInv.objects.filter(pub_date__date=(datetime.date.today())):
            date_for_show = datetime.date.today()
            print('today :', date_for_show)
        else:
            date_for_show = datetime.date.today() - datetime.timedelta(days=1)
            print ('yesterday :', date_for_show)
        self.assertEqual(Get_site('inv').status_code, 200)
        for c in range(100):
            a = random.choice(Sort_button_names)
            Sort_button_press = Get_site('inv', field_name = a)
            self.assertEqual(Sort_button_press.status_code, 200)

            Sort_by = System_var.objects.get(sys_field1=a).sys_field4 + a
            #print (Sort_by, "  :", c)
            table_sort = (list(
                Sort_button_press.context[-1]['table']) == list(
                CompInv.objects.filter(pub_date__date=date_for_show).order_by(Sort_by)))
            self.assertEqual(table_sort, True)
        List_of_names = CompInv.objects.values_list('user_name', flat=True).distinct()
        for names in List_of_names:
            print (names)
            self.assertEqual((self.client.get('/main/user_name/' + names + '/' )).status_code, 200)
        List_of_comps = CompInv.objects.values_list('comp_name', flat=True).distinct()
        for comps in List_of_comps:
            print (comps)
            self.assertEqual((self.client.get('/main/comp_name/' + comps + '/' )).status_code, 200)




