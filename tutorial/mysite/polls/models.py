from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField (max_length=200)
    pub_date = models.DateTimeField('date published')
    
    #Charfield is saying that is string / text and advising the max length and the format
    
    def __str__(self):
        return self.question_text
    #this line can be a string or any text, but in this case it is returning what was added as a question
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    choice_text = models.CharField (max_length=200)
    votes = models.IntegerField(default=0)
    
    #when we make a poll choice each of the choice are stored with a initial number of votes which starts at 0 and it goes up each time +1. 
    #cascade is usually what we use on databases 
    
    def __str__(self):
        return self.choice_text
    
    
