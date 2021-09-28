"""Определяет url адреса для этого приложения """
from django.urls import path #импортируется функция path
from .import views #для связывания URL с представлениями 

app_name = 'learning_logs'
urlpatterns = [
    # домашняя страница
    path('', views.index, name="index"),
    # страница со списком всех тем
    path('topics/', views.topics, name="topics"),
    # страница с информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name="topic"),
    # страница для добавления новой темы
    path('new_topic/', views.new_topic, name="new_topic"),
]



