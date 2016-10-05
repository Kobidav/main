from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Test_u(models.Model):
    Field_1 = models.CharField(max_length=200)
    Field_2 = models.CharField(max_length=200)
    Field_3 = models.CharField(max_length=200)
    Date_create = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.save()

    def remove(self):
        self.delete()

    def __str__(self):
        return self.Field_1


class CompInv(models.Model):
    comp_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    op_system = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    service_tag = models.CharField(max_length=200)
    processor = models.CharField(max_length=200)
    memory = models.CharField(max_length=200)
    date_boot = models.DateTimeField()
    upd_need = models.CharField(max_length=200)
    date_upd = models.DateTimeField()
    eset_nod = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    date_now = models.DateTimeField()
    comp_name_shot = models.CharField(max_length=200)  
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.comp_name
