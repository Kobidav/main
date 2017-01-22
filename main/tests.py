
from django.core.urlresolvers import reverse
from .models import CompInv, System_var, PhotoBase
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
import random



import datetime, time

def Field_to_None(list_in, field):
    for a in list_in:
        a[field] = None
    return list_in

CompInv_dic = Field_to_None(list(CompInv.objects.values()),'id')
System_var_dic = Field_to_None(list(System_var.objects.values()),'id')
PhotoBase_dic = Field_to_None(list(PhotoBase.objects.values()),'url_name')
Sort_button_names=('comp_name','user_name','date_boot','upd_need','eset_nod','pub_date')
count_of_check = 1


def upp_base(self):
    for l in CompInv_dic:
        m = CompInv.objects.create(**l)
        m.save()
    for l in System_var_dic:
        m = System_var.objects.create(**l)
        m.save()
    for l in PhotoBase_dic:
        m = PhotoBase.objects.create(**l)
        m.save()
    System_var.install()
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

class MainPageTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(MainPageTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MainPageTests, cls).tearDownClass()

    def test_base_load(self):
        def get_site(site, **kwargs):
            response = self.client.get(reverse(site), kwargs)
            return response
        upp_base(self)
        date_for_show = CompInv.objects.last().pub_date
        print ('last record :', date_for_show)
        # main page test**
        print ('test_base_load :',len(CompInv.objects.all()))
        self.selenium.get('%s%s' % (self.live_server_url, "/inv"))
        time.sleep(15)
        assert "Comp Inv" in self.selenium.title
        if self.selenium.find_element_by_xpath('//button[@value="inv"]'):
            print ("exist")
            self.selenium.find_element_by_xpath('//button[@value="inv"]').click()
        if not self.selenium.find_element_by_xpath('//button[@value="comp_name"]'):
            print("comp_name not exist")
        else:
            print("comp_name exist, click")
            self.selenium.find_element_by_xpath('//button[@value="comp_name"]').click()
            time.sleep(7)
            self.selenium.save_screenshot('/home/sysop/Desktop/screenshot.png')

        if not self.selenium.find_element_by_xpath('//button[@value="comp_name"]'):
            print("comp_name 2 not exist")
        else:
            print("comp_name 2 exist, click")
            self.selenium.find_element_by_xpath('//button[@value="comp_name"]').click()
            time.sleep(7)
            self.selenium.save_screenshot('/home/sysop/Desktop/screenshot2.png')





        self.assertEqual(get_site('inv').status_code, 200)
    def test_first(self):
        def get_site(site, **kwargs):
            response = self.client.get(reverse(site), kwargs)
            return response
        upp_base(self)
        date_for_show = CompInv.objects.last().pub_date

        print('test_first',len(CompInv.objects.all()))
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
    def test_names_pages(self):
        upp_base(self)
        date_for_show = CompInv.objects.last().pub_date
        print('test_names_pages',len(CompInv.objects.all()))
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
    def test_comp_pages(self):
        upp_base(self)
        date_for_show = CompInv.objects.last().pub_date
        print('test_comp_pages ',len(CompInv.objects.all()))
        list_of_comps = CompInv.objects.values_list('comp_name', flat=True).distinct()

        for comps in list_of_comps:
        # comps pages test**
            self.assertEqual(self.client.get(reverse('sort_n', kwargs={
                'stype': 'comp_name', 'svalue': comps})).status_code, 200)

            sort_button_press = self.client.get(reverse('sort_n', kwargs={
                'stype': 'comp_name', 'svalue': comps}))
            sort_by = []
            list_of_showing_data = list(CompInv.objects.filter(
                comp_name=comps).order_by(
                '-pub_date').values_list(
                'pub_date', flat=True)[0:8])
            table = CompInv.objects.filter(comp_name=comps).filter(
                pub_date__in=list_of_showing_data).order_by(
                *sort_by)
            table = hw_tooltip(table)
            table_sort = sort_button_press.context[-1]['table'] == table
            # users pages context test ****
            self.assertEqual(table_sort, True)
        #*****************************
            for c in range(count_of_check):
                random_fields_press = random.choice(Sort_button_names)
                sort_button_press = self.client.get(reverse('sort_n', kwargs = {
                'stype': 'comp_name', 'svalue': comps}),sys_field1=random_fields_press)
        # comp pages sorting test ****
                self.assertEqual(sort_button_press.status_code, 200)
        #***************************
    def test_hw_drop_pages(self):
        upp_base(self)
        date_for_show = CompInv.objects.last().pub_date
        print('test_hw_drop_pages ',len(CompInv.objects.all()))
        for hw_drop_module in hw_drop_list():
            for key in hw_drop_module[3]:
                link_hw_drop_menu = self.client.get(reverse('hard', kwargs={
                    'hwtype': hw_drop_module[0], 'hwvalue': hw_drop_module[3][key]}))
                self.assertEqual(link_hw_drop_menu.status_code, 200)







