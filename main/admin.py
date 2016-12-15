from django.contrib import admin
from .models import CompInv
from .models import System_var
from .models import PhotoBase


admin.site.register(System_var)
admin.site.register(CompInv)
admin.site.register(PhotoBase)


