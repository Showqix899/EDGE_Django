from django.db import models

# Create your models here.

#defining a publisher
class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


#defining a data model for Author
class Author(models.Model):

    name=models.CharField(max_length=150)
    birth_date=models.DateField()

    def __str__(self):

        return self.name



class BookManager(models.Manager):


    def get_published_books(self):
        
        return self.filter(is_published=True)  


#defining a data model for Book

class Book(models.Model):

    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    publication_date=models.DateField()
    is_published=models.BooleanField(default=False)
    description=models.TextField(max_length=600, null=True,blank=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE,null=True,blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True,blank=True)

    objects=BookManager()

    def __str__(self):
        return self.title
