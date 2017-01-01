from django.db import models
from .nod import Eset_version
from datetime import datetime


class CompInv(models.Model):
    comp_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    op_system = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    service_tag = models.CharField(max_length=200,blank=True)
    processor = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    date_boot = models.DateTimeField()
    upd_need = models.IntegerField(blank=True)
    date_upd = models.DateTimeField(blank=True,null=True)
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
    url_name = models.CharField(max_length=1000,blank=True,null=True)
    mail_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sam_name + "(" + self.site_name + ")"




class System_var(models.Model):
    desc_name = models.CharField(max_length=200)
    sys_field1 = models.CharField(max_length=200)
    sys_field2 = models.CharField(max_length=200)
    sys_field3 = models.CharField(max_length=200,blank=True)
    sys_field4 = models.CharField(max_length=200,blank=True)
    sys_field5 = models.CharField(max_length=200,blank=True)
    sys_field6 = models.IntegerField()

    def __str__(self):
        return self.desc_name + "(" + self.sys_field1 + ")"

    def get_nod():
        Eset_version.get()
        return System_var.objects.filter(desc_name="eset_nod_act_v").update(
            sys_field1=Eset_version.version,
            sys_field2=Eset_version.data,
            sys_field6=int(Eset_version.version) - 10)
    def Sort_Update(field_name):
        if field_name == 'zero':
            for sys_f3 in System_var.objects.filter(desc_name='sort_buttons_arrows'):
                System_var.objects.filter(sys_field1=sys_f3.sys_field1).update(sys_field3='',sys_field4='')
            return 'reset fields'


        if System_var.objects.filter(desc_name='sort_buttons_arrows').get(sys_field1=field_name).sys_field3 == 'glyphicon-menu-down':
            System_var.objects.filter(sys_field1=field_name).update(sys_field3='glyphicon-menu-up',sys_field4='')
            return field_name + ' up'
        else:
            for sys_f3 in System_var.objects.filter(desc_name='sort_buttons_arrows'):
                System_var.objects.filter(sys_field1=sys_f3.sys_field1).update(sys_field3='',sys_field4='-')
            System_var.objects.filter(sys_field1=field_name).update(sys_field3='glyphicon-menu-down')
            return field_name + ' down'
    def Show_Data(show_data):
        if show_data== "all":
            System_var.objects.filter(desc_name="type_of_view").update(
                sys_field5='2016-10-19',
                sys_field1='All Data',
                sys_field4='btn-info disabled',
                sys_field3='btn-primary')
        else:

            System_var.objects.filter(desc_name="type_of_view").update(
                sys_field5=str(CompInv.objects.last().pub_date.date()),
                sys_field1='Last Record',
                sys_field3='btn-info disabled',
                sys_field4='btn-primary')
