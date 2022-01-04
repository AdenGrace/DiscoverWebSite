from django.contrib import admin
from .models import Area, Customer, Drivers, Instructor
from .models import MyUsers
from .models import Trips
from .models import User

admin.site.register(Area)
admin.site.register(MyUsers)
admin.site.register(Trips)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Drivers)
admin.site.register(Instructor)

