from django.shortcuts import render, redirect
from .models import Topic 
from .forms import TopicForm

# Create your views here.

def index(request): #"""Домашняя страница приложения Learning Log"""
    return render(request, "learning_logs/index.html")


def topics(request):
    """ выводит список этих тем """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, "learning_logs/topics.html", context)


def topic(request, topic_id):
    """ выводит одну тему и все ее записи """
    topic = Topic.objects.get(id=topic_id) #функция get() используется для получения темы 
    entries = topic.entry_set.order_by('-date_added') # сортирует результаты в обратном порядке
    context = {'topic': topic, 'entries': entries} #Тема и записи сохраняются в словаре context 
    return render(request, 'learning_logs/topic.html', context) #передается шаблону topic.html

def new_topic(request):
    """ определяет новую тему """
    if request.method != 'POST': 
        # если данные не отправлялись, создается пустая форма
        form = TopicForm()
    else:
        #отправлены данные POST , обработать данные 
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    #вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)