from django.db import models

# Create your models here.


class NoOccurentData(models.Model):
    objects = None
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=40, blank=True, null=False)


class Grade(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class TypePoste(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class Poste(NoOccurentData):
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_type_poste = models.OneToOneField(TypePoste, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}({self.fk_type_poste.name})'


class TypeDepartment(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class Department(NoOccurentData):
    description = models.CharField(max_length=255, blank=True, null=True)
    fk_type_departments = models.OneToOneField(TypeDepartment, on_delete=models.CASCADE)


class TypeProfession(NoOccurentData):

    def __str__(self):
        return f'{self.name}'


class Profession(NoOccurentData):
    fk_type_profession = models.ForeignKey(TypeProfession, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}({self.fk_type_profession.name})'


class Employee(NoOccurentData):
    name = None
    first_name = models.CharField(max_length=40, blank=True, null=False)
    last_name = models.CharField(max_length=40, blank=True, null=False)
    date_birthday = models.DateTimeField(null=False)
    marital_status = models.CharField(max_length=12, blank=True, null=False)
    level_of_study = models.CharField(max_length=255, blank=True, null=False)
    job_description = models.CharField(max_length=255, blank=True, null=False)
    fk_poste = models.OneToOneField(Poste, on_delete=models.CASCADE)
    fk_profession = models.OneToOneField(Profession, on_delete=models.CASCADE)
    fk_department = models.OneToOneField(Department, on_delete=models.CASCADE)


class AdresseEmployee(NoOccurentData):
    city = models.CharField(max_length=25, blank=True, null=False)
    street = models.CharField(max_length=255, blank=True, null=False)
    fk_employee = models.OneToOneField(Employee, on_delete=models.CASCADE)




