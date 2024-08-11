from django.db import models
from django.contrib.auth.models import User

#Model~2: Label
class Label(models.Model):
    name = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, 
                              related_name = 'label_relationship', 
                              on_delete = models.CASCADE)
    
    #Avoiding Duplicates using Meta class
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ["owner", "name"], 
                                    name = "the_owner")
        ]
    
    def __str__(self):  
        return self.name
    
#Model~1: Task
class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    completion_status = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, 
                              related_name ='tasks', 
                              on_delete = models.CASCADE)
    label_relationship = models.ManyToManyField(Label, 
                                                related_name = 'tasks')



    def __str__(self):
        return self.title