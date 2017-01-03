
from django.core.urlresolvers import reverse
from .models import CompInv, System_var, PhotoBase
from django.test import TestCase
import random


import datetime
print ('1')
def Field_to_None(list_in, field):
    for a in list_in:
        a[field] = None
    return list_in

CompInv_dic = Field_to_None(list(CompInv.objects.values()),'id')
System_var_dic = Field_to_None(list(System_var.objects.values()),'id')
PhotoBase_dic = Field_to_None(list(PhotoBase.objects.values()),'url_name')
Sort_button_names=('comp_name','user_name','date_boot','upd_need','eset_nod','pub_date')





class MainPageTests(TestCase):
    print ('hello')


    def test_inv_variables_validation(self):
        count_of_check = 10
        def get_site(site, **kwargs):

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
            date_for_show = CompInv.objects.last().pub_date
            print ('last record :', date_for_show)
        self.assertEqual(get_site('inv').status_code, 200)
        for c in range(count_of_check):
            random_fields_press = random.choice(Sort_button_names)
            sort_button_press = get_site('inv', field_name = random_fields_press)
            self.assertEqual(sort_button_press.status_code, 200)

            sort_by = System_var.objects.filter(desc_name='sort_buttons_arrows').get(sys_field1=random_fields_press).sys_field4 + random_fields_press
            print (sort_by, "  :", c)
            table_sort = (list(
                sort_button_press.context[-1]['table']) == list(
                CompInv.objects.filter(pub_date__date=date_for_show).order_by(sort_by)))
            self.assertEqual(table_sort, True)
        list_of_names = CompInv.objects.values_list('user_name', flat=True).distinct()
        for names in list_of_names:
            print (names)
            self.assertEqual(self.client.get(reverse('sort_n', kwargs = {
                'stype': 'user_name', 'svalue': names})).status_code, 200)
            sort_button_press=self.client.get(reverse('sort_n', kwargs={
                'stype': 'user_name', 'svalue': names}))
            Sort_by=[]
            list_of_showing_data = list(
                CompInv.objects.filter(user_name=names).order_by('-pub_date').values_list('pub_date', flat=True)[0:8])
            table = CompInv.objects.filter(user_name=names).filter(pub_date__in=list_of_showing_data).order_by(
                *Sort_by)
            table_sort = (list(
                sort_button_press.context[-1]['table']) == list(table))

            self.assertEqual(table_sort, True)
            System_var.Sort_Update('zero')
            for c in range(count_of_check):
                sort_button_press = self.client.get(reverse('sort_n', kwargs = {
                'stype': 'user_name', 'svalue': names}),sys_field1=random_fields_press)
                self.assertEqual(sort_button_press.status_code, 200)

        list_of_comps = CompInv.objects.values_list('comp_name', flat=True).distinct()
        for comps in list_of_comps:
            print (comps)
            self.assertEqual(self.client.get(reverse('sort_n', kwargs={
                'stype': 'comp_name', 'svalue': comps})).status_code, 200)
            System_var.Sort_Update('zero')
            for c in range(count_of_check):
                sort_button_press = self.client.get(reverse('sort_n', kwargs = {
                'stype': 'comp_name', 'svalue': comps}),sys_field1=random_fields_press)
                self.assertEqual(sort_button_press.status_code, 200)






