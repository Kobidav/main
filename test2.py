

from main.models import PhotoBase
from main.get_photo import list_of_image


UsersNames = PhotoBase.objects.values_list('u_name', flat=True)
UsersSurNames = PhotoBase.objects.values_list('so_name', flat=True)

print("hello")
