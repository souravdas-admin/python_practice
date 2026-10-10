from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    total_copies = models.IntegerField()
    available_copies = models.IntegerField()
    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    membership_date = models.DateField()
    def __str__(self):
        return self.name

class BookIssue(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return f'{self.book}--{self.member}'
