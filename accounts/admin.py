from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Appointment)
admin.site.register(Event)
admin.site.register(DiscussTopic)
admin.site.register(DiscussConversation)
