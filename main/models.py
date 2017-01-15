from django.db import models
from .nod import Eset_version
from datetime import datetime


class CompInv(models.Model):
    comp_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    op_system = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    service_tag = models.CharField(max_length=200, blank=True)
    processor = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    date_boot = models.DateTimeField()
    upd_need = models.IntegerField(blank=True)
    date_upd = models.DateTimeField(blank=True, null=True)
    eset_nod = models.IntegerField(blank=True)
    pub_date = models.DateTimeField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.comp_name


class PhotoBase(models.Model):
    sam_name = models.CharField(max_length=200, unique=True)
    u_name = models.CharField(max_length=200)
    so_name = models.CharField(max_length=200)
    site_name = models.CharField(max_length=200)
    url_name = models.CharField(max_length=1000, blank=True, null=True)
    mail_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sam_name + "(" + self.site_name + ")"


class System_var(models.Model):
    desc_name = models.CharField(max_length=200)
    sys_field1 = models.CharField(max_length=200)
    sys_field2 = models.CharField(max_length=200)
    sys_field3 = models.CharField(max_length=200, blank=True)
    sys_field4 = models.CharField(max_length=200, blank=True)
    sys_field5 = models.CharField(max_length=200, blank=True)
    sys_field6 = models.IntegerField()

    def __str__(self):
        return self.desc_name + "(" + self.sys_field1 + ")"

    def get_nod():
        Eset_version.get()
        return System_var.objects.update_or_create(
            desc_name="eset_nod_act_v", defaults={
            'sys_field1':Eset_version.version,
            'sys_field2':Eset_version.data,
            'sys_field3':'',
            'sys_field4':'Blank',
            'sys_field5':'Blank',
            'sys_field6':(int(Eset_version.version) - 10)})

    def Sort_Update(field_name):
        if field_name == 'zero':
            list_of_fields=[['comp_name','Comp Name'],
                            ['user_name','User Name'],
                            ['date_boot','Date Boot'],
                            ['upd_need','Update Need'],
                            ['eset_nod','Nod Version'],
                            ['pub_date', 'Date']]
            for sys_field in list_of_fields:
                System_var.objects.update_or_create(
                    desc_name="sort_buttons_arrows", sys_field1= sys_field[0], defaults={
                        'sys_field1': sys_field[0],
                        'sys_field2': sys_field[1],
                        'sys_field3': '',
                        'sys_field4': '',
                        'sys_field5': 'Blank',
                        'sys_field6': 1})
        else:
            if System_var.objects.filter(
                desc_name='sort_buttons_arrows').get(
                sys_field1=field_name).sys_field3 == 'glyphicon-menu-down':
                System_var.objects.filter(
                    sys_field1=field_name).update(
                    sys_field3='glyphicon-menu-up', sys_field4='')
            else:
                for sys_f3 in System_var.objects.filter(
                        desc_name='sort_buttons_arrows'):
                    System_var.objects.filter(
                        sys_field1=sys_f3.sys_field1).update(
                        sys_field3='', sys_field4='-')
                System_var.objects.filter(
                    sys_field1=field_name).update(
                    sys_field3='glyphicon-menu-down')
            



    def Show_Data(show_data):
        if show_data == "day_all":
            System_var.objects.update_or_create(
                desc_name="type_of_view", defaults={
                'sys_field5':'2016-10-19',
                'sys_field1':'Last Record',
                'sys_field3':'day',
                'sys_field2': 'null',
                'sys_field6': 1,
                'sys_field4':'All Data'})
        else:
            System_var.objects.update_or_create(
                desc_name="type_of_view", defaults={
                'sys_field5':str(CompInv.objects.last().pub_date.date()),
                'sys_field1':'All Data',
                'sys_field3':'day_all',
                'sys_field2': 'null',
                'sys_field6': 1,
                'sys_field4':'Last Record'})

    def Create_hw_tables():
        list_of_fields = [['op_system', 'System'],
                          ['model_name', 'Model'],
                          ['service_tag', 'Service Tag'],
                          ['processor', 'Processor'],
                          ['memory', 'Memory'],
                          ['comp_name', 'Comp Name']]

        for sys_field in list_of_fields:
            System_var.objects.update_or_create(
                desc_name="sort_buttons_arrows_hw", sys_field1= sys_field[0], defaults={
                    'sys_field1': sys_field[0],
                    'sys_field2': sys_field[1],
                    'sys_field3': '',
                    'sys_field4': '',
                    'sys_field5': 'drop_list',
                    'sys_field6': 0})
    def install():
        System_var.Show_Data('zero')
        System_var.Create_hw_tables()
        System_var.Sort_Update('zero')
        System_var.get_nod()



