
from django.urls import path
from . views import blog
urlpatterns = [
    path('bg/',blog, name="blog")

]
