from django.contrib import admin
from .models import (Grade, Employee, Poste, Profession, TypeProfession, TypePoste, Department, AdresseEmployee,
                     TypeDepartment)

admin.site.register(Grade)
admin.site.register(Employee)
admin.site.register(Poste)
admin.site.register(Profession)
admin.site.register(TypeProfession)
admin.site.register(TypePoste)
admin.site.register(Department)
admin.site.register(AdresseEmployee)
admin.site.register(TypeDepartment)

