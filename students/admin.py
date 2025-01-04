from django.contrib import admin
from .models import Student, Countries, University, Subjects, Application, PrimaryStatus, SecondaryStatus

admin.site.register(Student)
admin.site.register(Countries)
admin.site.register(University)
admin.site.register(Subjects)
admin.site.register(Application)
admin.site.register(PrimaryStatus)
admin.site.register(SecondaryStatus)

