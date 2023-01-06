from django.urls import path
from . views import tasklist, taskDetail,taskCreate,taskUpdate,DeleteView,CustomloginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomloginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page="login"),name='logout'),
    path('register/',RegisterPage.as_view(), name='register'),

    path('',tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/',taskDetail.as_view(), name='task'),
    path('task-create/',taskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/',taskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',DeleteView.as_view(), name='task-delete'),
    
]
