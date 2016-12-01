from django.contrib import admin
from .models import CompInv
from .models import System
from .models import PhotoBase
from .models import Sort_button

admin.site.register(System)
admin.site.register(CompInv)
admin.site.register(PhotoBase)
admin.site.register(Sort_button)

