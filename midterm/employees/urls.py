from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViesSet

router = DefaultRouter()
router.register('employees', EmployeeViesSet)

urlpatterns = []

urlpatterns += router.urls
