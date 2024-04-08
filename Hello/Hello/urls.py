
from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Harsh Gym Admin"
admin.site.site_title = "Harsh Gym Admin Portal"
admin.site.index_title = "Welcome to Harsh Gym Admin Panel"


urlpatterns = [
     path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
