from django.db import models
from .nod import Eset_version


class CompInv(models.Model):
    comp_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    op_system = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    service_tag = models.CharField(max_length=200)
    processor = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    date_boot = models.DateTimeField()
    upd_need = models.IntegerField()
    date_upd = models.DateTimeField()
    eset_nod = models.IntegerField()
    pub_date = models.DateTimeField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.comp_name


class System(models.Model):
    desc_name = models.CharField(max_length=200)
    sys_field1 = models.CharField(max_length=200)
    sys_field2 = models.CharField(max_length=200)
    sys_field3 = models.CharField(max_length=200)
    sys_field4 = models.CharField(max_length=200)
    sys_field5 = models.CharField(max_length=200)
    sys_field6 = models.IntegerField()

    def __str__(self):
        return self.desc_name + "(" + self.sys_field1 + ")"

    def get_nod():
        Eset_version.get()
        return System.objects.filter(desc_name="eset_nod_act_v").update(
            sys_field1=Eset_version.version,
            sys_field2=Eset_version.data,
            sys_field6=int(Eset_version.version) - 10)


class PhotoBase(models.Model):
    sam_name = models.CharField(max_length=200, unique=True)
    u_name = models.CharField(max_length=200)
    so_name = models.CharField(max_length=200)
    site_name = models.CharField(max_length=200)
    url_name = models.CharField(max_length=1000)
    mail_name = models.CharField(max_length=200)

    def __str__(self):
        return self.sam_name + "(" + self.site_name + ")"
