from django.contrib import admin
from django.urls import path
from todo_list import views as todo_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todo_views.Attendance, name='Attendance'),
    path('delete/<list_id>', todo_views.delete, name='delete'),
    path('edit/<list_id>', todo_views.edit, name='edit'),
]
