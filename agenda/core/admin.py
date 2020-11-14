from django.contrib import admin
from core.models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


admin.site.register(UserProfile, UserProfileAdmin)
