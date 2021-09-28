from django.db import models

# Create your models here.

class Topic(models.Model):
    """ Тема, которую изучает пользователь """
    text = models.CharField(max_length=56) #это модель кот имеет свойство написать до 200 символов
    date_added = models.DateTimeField(auto_now_add=True) #дает возможность показывать дату и время
    
    def __str__(self):
        """ Возвращает строковое представление модели"""
        return self.text 

class Entry(models.Model):
    """ Информация изученная пользователем по теме"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE) 
    text = models.TextField() #неограничен в символах
    date_added = models.DateTimeField(auto_now_add=True) #дату и время
    
    class Meta: #дополнение к классу ентри
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """ дает возможность отформатировать поле 
        Возвращает строковое представление модели """
        return f"{self.text[:50]}..." #show more
    
    
    