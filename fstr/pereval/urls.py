from django.urls import path
from . import views

urlpatterns = [
    path('submitData/', views.SubmitDataView.as_view(), name='pereval-list'),
    path('submitData/<int/pk>', views.SubmitDataView.as_view(), name='pereval-detail'),
]