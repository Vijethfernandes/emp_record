from django.contrib import admin
from emp_app.models import Employee,Role,Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Role)