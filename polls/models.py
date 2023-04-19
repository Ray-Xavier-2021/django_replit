from secrets import choice
from django.db import models

# Create your models here.

# Inheritis everything in Model
# Questions class
class Question(models.Model):
    # Specify fields
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Return response as a string
    def __str__(self):
        return self.question_text

# Answers class
class Choice(models.Model):
    # Link relation to question_idand choice using ForeignKey
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Fields
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Return response as a string
    def __str__(self):
        return self.choice_text