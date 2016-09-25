# tutorial/tables.py
import django_tables2 as tables
from .models import Post
from .models import CompInv


class PersonTable(tables.Table):
    class Meta:
        model = CompInv
        # add class="paleblue" to <table> tag
        # attrs = {'class': 'paleblue'}
        per_page = 300
        fields = ('comp_name', 'user_name', 'date_boot',
                  'upd_need', 'date_upd', 'eset_nod')
    date_upd = tables.Column(verbose_name='Last Update Check' ,localize=False)
    date_boot = tables.Column(localize=False)
    pub_date = tables.Column(localize=False)


class PersonTable2(tables.Table):
    class Meta:
        model = CompInv
        per_page = 300
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}
        #fields = ('comp_name', 'user_name', 'date_boot', 'upd_need', 'date_upd', 'esed_nod')
