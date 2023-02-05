from django.urls import path
from . import views

urlpatterns = [
    path('<int:lot_id>', views.detail, name='detail'),
]
