from django.urls import path
from .views import MyView, MyViewReq, BaseRegisterView, NoteCreate, CalendarView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', MyView.as_view()),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('req/', MyViewReq.as_view()),
    path('signup/', BaseRegisterView.as_view(template_name='sign.html'), name='signup'),
    path('note/create/', NoteCreate.as_view(), name='note_create'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    ]