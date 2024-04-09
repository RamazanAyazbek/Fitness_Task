from rest_framework import routers
from django.urls import include, path
from .views import AppointmentViewAPI, TrainerViewAPI


router=routers.DefaultRouter()
router.register(r'api/appointment', AppointmentViewAPI)
router.register(r'api/trainer', TrainerViewAPI)



urlpatterns=[
  path('', include(router.urls))
]









