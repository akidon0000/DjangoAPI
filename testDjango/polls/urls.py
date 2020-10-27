#app.urls

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from polls import views

urlpatterns = [
    path('api/user/', views.user_list),
    path('api/user/<int:pk>/',views.user_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)