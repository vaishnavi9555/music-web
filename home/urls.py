from django.urls import path
from .views import home, upload
urlpatterns = [
    path('', home, name='home')
]

htmx_patterns= [
    path('upload/',upload, name='upload')
]

urlpatterns += htmx_patterns