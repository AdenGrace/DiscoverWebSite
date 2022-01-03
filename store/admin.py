from django.contrib import admin
from .models import Area
from .models import MyUsers
from .models import Trips
from .models import User

admin.site.register(Area)
admin.site.register(MyUsers)
admin.site.register(Trips)

