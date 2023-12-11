from django.urls import path
from . views import MenueItemView,SingleMenueItemView



urlpatterns = [
    path('menue-item',MenueItemView.as_view()),
    path('menue-item/<int:pk>',SingleMenueItemView.as_view())
]

