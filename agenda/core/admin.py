from django.contrib import admin
from core.models import User, ClienteProfile, MedicoProfile, ClinicaProfile, Especialidade, MedicoEspecialidade, Agenda
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['descricao']


class MedicoEspecialidadeAdmin(admin.ModelAdmin):
    list_display = ['medico', 'especialidade']


class AgendaAdmin(admin.ModelAdmin):
    list_display = ['data_agenda', 'clinica', 'especialidade', 'medico']


admin.site.register(User, UserAdmin)
admin.site.register(ClienteProfile, UserProfileAdmin)
admin.site.register(MedicoProfile, UserProfileAdmin)
admin.site.register(ClinicaProfile, UserProfileAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(MedicoEspecialidade, MedicoEspecialidadeAdmin)
admin.site.register(Agenda, AgendaAdmin)
