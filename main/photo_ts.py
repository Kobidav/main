

from .models import PhotoBase
from .get_photo import list_of_image


UsersNames = PhotoBase.objects.values_list('u_name', flat=True).exclude(u_name='')
UsersSurNames = PhotoBase.objects.values_list('so_name', flat=True).exclude(so_name='')

print("hello")
