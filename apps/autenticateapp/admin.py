from django.contrib import admin
from .models import DisplayModel,PatientModel,DoctorModel,AppointmentModel
# Register your models here.


admin.site.register(DisplayModel)

admin.site.register(PatientModel)

admin.site.register(DoctorModel)

admin.site.register(AppointmentModel)

