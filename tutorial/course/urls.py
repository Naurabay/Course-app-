from django.urls import path
from course import views


urlpatterns = [
    path('', views.CourseList.as_view(), name='courseList'),
    path('course<int:pk>/', views.CourseDetail.as_view(), name='courseDetail'),

]
