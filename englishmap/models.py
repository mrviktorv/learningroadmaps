from django.db import models
from ckeditor.fields import RichTextField
from django. urls import reverse

class Topic(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    
    title = models.CharField(max_length=100)
    # short = models.TextField()
    short = RichTextField()
    full = RichTextField()
    fullest = RichTextField()
    test = RichTextField(blank=True, null=True)
    add = RichTextField(blank=True, null=True)

    
    def firstletter(self):
        return self.title[0].upper()

    def __str__(self):
        # change this to id + name
        return f'{self.id} {self.title}'

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.name}'

    @property
    def get_replies(self):
        return self.replies.all()       

class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies',  on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    nameR = models.CharField(max_length=100)
    bodyR = models.TextField()

    def __str__(self):
        return f'{self.id} {self.nameR}'

class LayoutRow(models.Model):
    arrL = models.CharField(max_length=50, blank=True, null=True)
    arrC = models.CharField(max_length=50, blank=True, null=True)
    arrR = models.CharField(max_length=50, blank=True, null=True)
    topL = models.PositiveIntegerField(blank=True, null=True)
    topC = models.PositiveIntegerField(blank=True, null=True)
    topR = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)

class LayoutRow1(models.Model):
    arrL = models.CharField(max_length=50, blank=True, null=True)
    arrC = models.CharField(max_length=50, blank=True, null=True)
    arrR = models.CharField(max_length=50, blank=True, null=True)
    topL = models.PositiveIntegerField(blank=True, null=True)
    topC = models.PositiveIntegerField(blank=True, null=True)
    topR = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.id)