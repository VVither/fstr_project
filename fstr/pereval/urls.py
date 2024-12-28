from django.urls import path
from . import views

urlpatterns = [
    path('submitData/', views.SubmitDataView.as_view(),),
    path('submitData/<int/pk>', views.SubmitDataView.as_view()),
]