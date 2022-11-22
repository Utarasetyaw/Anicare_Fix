from knox import views as knox_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register/patient/', RegisterPatientAPI.as_view(), name="patient registration"),
    path('register/doctor/', RegisterDoctorAPI.as_view(), name="doctor registration"),
    path('register/admin/', RegisterAdminAPI.as_view(), name="admin registration"),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='test'),
    path('password/', ChangePasswordView.as_view(), name='change password'),
    path('delete/', DeleteAccountView.as_view(), name='delete account'),
    path('admin/delete-user/', DeleteTargetAccountView.as_view(), name='delete specific account'),
    path('admin/acc-doctor/', AccDoctorView.as_view(), name='acc doctor'),
    path('appointment/', AppointmentView.as_view(), name="Get and Create Appointment"),
    path('appointment/status/', ChangeStatusAppointmentView.as_view(), name="Get and Create Appointment"),
    path('discuss/', DiscussView.as_view(), name="Create a Topic discussion"),
    path('discuss/all', DiscussAll.as_view(), name="Create a Topic discussion"),
    path('discuss/<int:id_topic>', DiscussView.as_view(), name="View and delete the topic"),
    path('discuss/<int:id_topic>/comment/', DiscussConversationView.as_view(), name="Post a Comment to discussion"),
    path('discuss/<int:id_topic>/comment/<int:id_comment>', DiscussConversationView.as_view(), name="Delete a comment in a Topic discussion"),
    path('events/<int:id_event>', EventsView.as_view(), name="View Event"),
    path('events/all', EventAll.as_view(), name="View Event"),
    path('admin/events/', EventsCreateView.as_view(), name="Create an event"),
    path('admin/events/<int:id_event>', EventsCreateView.as_view(), name="Delete an event"),
    path('chat/', Chatbot.as_view(), name="Get and set AI")
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)