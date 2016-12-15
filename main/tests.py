
from django.core.urlresolvers import reverse
from .models import CompInv, System_var, PhotoBase
from django.test import TestCase
import random


import datetime

def Id_to_None(list_in):
    for a in list_in:
        a['id'] = None
    return list_in

CompInv_dic = Id_to_None(list(CompInv.objects.values()))
System_var_dic = Id_to_None(list(System_var.objects.values()))
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
            print (Sort_by, "  :", c)
            table_sort = (list(
                Sort_button_press.context[-1]['table']) == list(
                CompInv.objects.filter(pub_date__date=date_for_show).order_by(Sort_by)))
            self.assertEqual(table_sort, True)



        # if CompInv.objects.filter(pub_date__date=(datetime.date.today())):
        #     table_today = (list(
        #         Get_site('inv').context[-1]['table']) == list(
        #         CompInv.objects.filter(pub_date__date=(datetime.date.today()))))
        #     print('today :', table_today)
        #     self.assertEqual(table_today, True)
        # else:
        #     table_yesterday = (list(
        #         Get_site('inv').context[-1]['table']) == list(
        #         CompInv.objects.filter(pub_date__date=(datetime.date.today() - datetime.timedelta(days=1)))))
        #     print ('yesterday :', table_yesterday)
        #     self.assertEqual(table_yesterday, True)




