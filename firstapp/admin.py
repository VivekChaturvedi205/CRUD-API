from django.contrib import admin
from firstapp.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('FirstName','LastName','Gender','DOB','Salutation','Designation','Email','Mobile','AddressLine1','AddressLine2','City','State','Pin','Country')
