from rest_framework import routers
from .views import (GradeViewSet, PosteViewSet, ProfessionViewSet, TypePosteViewSet, EmployeeViewSet,
                    AdresseEmployeeViewSet, TypeProfessionViewSet, TypeDepartmentViewSet, DepartmentViewSet)

router = routers.DefaultRouter()

router.register(r'adresse/employee', AdresseEmployeeViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'grade', GradeViewSet)
router.register(r'poste', PosteViewSet)
router.register(r'profession', ProfessionViewSet)
router.register(r'type/department', TypeDepartmentViewSet)
router.register(r'type/poste', TypePosteViewSet)
router.register(r'type/profession', TypeProfessionViewSet)

urlpatterns = router.urls
