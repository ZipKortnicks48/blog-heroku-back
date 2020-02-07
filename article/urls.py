from django.urls import path
from .views import ContentLenthView,SingleContentView
app_name = "article"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('contents/', ContentLenthView.as_view()),
    path('contents/<int:pk>', SingleContentView.as_view()),
]
