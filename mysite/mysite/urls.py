from django.contrib import admin
from django.urls import include, path
from django.conf import settings

admin.site.site_header ="King's Administration"
admin.site.site_title = "King's Administration"
admin.site.index_title = 'index title'

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    
]
