from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)

#>pip install mysql_connector_python
#>pip install pymysql