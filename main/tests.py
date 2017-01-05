
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
        count_of_check = 5
        def get_site(site, **kwargs):

            response = self.client.get(reverse(site), kwargs)
            return response
        def hw_tooltip(table):
            if type(table) is list:
                comp_list = []
                for units in table:
                    comp_list.append(units.comp_name)
            else:
                comp_list = table.values_list("comp_name", flat=True)
            list_of_hw_tooltip = []
            for comp in comp_list:
                string_data = CompInv.objects.filter(comp_name=comp).latest('pub_date')
                unit_of_list = " || ".join([
                    string_data.model_name,
                    string_data.processor,
                    string_data.memory,
                    string_data.service_tag])
                list_of_hw_tooltip.append(unit_of_list)
            table = zip(table, list_of_hw_tooltip)
            list_of_hw_tooltip = []
            for a, b in table:
                list_of_hw_tooltip.append([a, b])
            return list_of_hw_tooltip
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
# main page test**
        self.assertEqual(get_site('inv').status_code, 200)
#*****************
        for c in range(count_of_check):
            random_fields_press = random.choice(Sort_button_names)
            sort_button_press = get_site('inv', field_name = random_fields_press)
# main page sorting test ***
            self.assertEqual(sort_button_press.status_code, 200)
#****************************
            sort_by = System_var.objects.filter(
                desc_name='sort_buttons_arrows').get(
                sys_field1=random_fields_press).sys_field4 + random_fields_press
            table = CompInv.objects.filter(pub_date__date=date_for_show).order_by(sort_by)
            table = hw_tooltip(table)
            table_sort = sort_button_press.context[-1]['table'] == table
# main page context sorting test ***
            self.assertEqual(table_sort, True)
#**********************
        list_of_names = CompInv.objects.values_list('user_name', flat=True).distinct()
        for names in list_of_names:
# user pages test**
            self.assertEqual(self.client.get(reverse('sort_n', kwargs = {
                'stype': 'user_name', 'svalue': names})).status_code, 200)
#************************
            sort_button_press=self.client.get(reverse('sort_n', kwargs={
                'stype': 'user_name', 'svalue': names}))
            sort_by=[]
            list_of_showing_data =list(CompInv.objects.filter(
                user_name=names).order_by(
                '-pub_date').values_list(
                'pub_date', flat=True)[0:8])
            table = CompInv.objects.filter(user_name=names).filter(
                pub_date__in=list_of_showing_data).order_by(
                *sort_by)
            table = hw_tooltip(table)
            table_sort = sort_button_press.context[-1]['table'] == table
# users pages context test ****
            self.assertEqual(table_sort, True)
#*********************************
            System_var.Sort_Update('zero')
            for c in range(count_of_check):
                random_fields_press = random.choice(Sort_button_names)
                sort_button_press = self.client.get(reverse('sort_n', kwargs = {
                'stype': 'user_name', 'svalue': names}),sys_field1=random_fields_press)
# users pages context sorting test ****
                self.assertEqual(sort_button_press.status_code, 200)
#**********************************

        list_of_comps = CompInv.objects.values_list('comp_name', flat=True).distinct()

        for comps in list_of_comps:
# comps pages test**
            self.assertEqual(self.client.get(reverse('sort_n', kwargs={
                'stype': 'comp_name', 'svalue': comps})).status_code, 200)
#*****************************
            System_var.Sort_Update('zero')
            for c in range(count_of_check):
                random_fields_press = random.choice(Sort_button_names)
                sort_button_press = self.client.get(reverse('sort_n', kwargs = {
                'stype': 'comp_name', 'svalue': comps}),sys_field1=random_fields_press)
# comp pages sorting test ****
                self.assertEqual(sort_button_press.status_code, 200)
#***************************






