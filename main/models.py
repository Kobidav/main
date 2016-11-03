from django.db import models


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
    date_now = models.DateTimeField()
    comp_name_shot = models.CharField(max_length=200)

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

    def __str__(self):
        return self.desc_name + "(" + self.sys_field1 + ")"
