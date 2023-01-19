
from django.contrib import admin
from django.urls import path
from school.views import homepage ,deleteStudent, editStudent, searchStudent, filtercity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('delete/<int:id>/', deleteStudent , name ='delete'),
    path('edit/<int:id>/', editStudent, name='edit'),
    path('search/', searchStudent, name='search'),
    path('filter-city',filtercity, name='filter')
]
