from django.urls import path
from .views import blog_page,blog_detail


urlpatterns = [
    path('',blog_page,name='bpage'),
    path('<int:id>/',blog_detail,name='detail')
]