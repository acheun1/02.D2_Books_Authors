from django.db import models


# Please do the following

# Create a new model called 'Book' with the information above.
# Create a new model called 'Author' with the information above.  Design the models in a way that you could perform the following:
    # Book.objects.first().authors
    # Author.objects.first().books
# Successfully create and run the migration files
# Using the shell...

# Create your models here.
class UserManager(models.Manager):
    pass

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes=models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    authors=models.ManyToManyField(Author, related_name="authors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

#from apps.app_01.models import *

# Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
# Book.objects.create(name="C Sharp")
# Book.objects.create(name="Java")
# Book.objects.create(name="Python")
# Book.objects.create(name="PHP")
# Book.objects.create(name="Ruby")

# Create 5 different authors: Mike, Speros, John, Jadee, Jay

#Author.objects.create(first_name="Mike")
#Author.objects.create(first_name="Speros")
#Author.objects.create(first_name="John")
#Author.objects.create(first_name="Jadee")
#Author.objects.create(first_name="Jay")

# Add a new field in the authors table called 'notes'.  Make this a TextField.  Successfully create and run the migration files.

# Using the shell...
# Change the name of the 5th book to C#
#   update1 = Book.objects.get(id=5)
#   update1.name = "C#"
#   update1.save()
# Change the first_name of the 5th author to Ketul
#   update2= Author.objects.get(id=5)
#   update2.first_name= "Ketul"
#   update2.save()
# Assign the first author to the first 2 books
#   update3=Book.objects.get(id=2)
#   update3.Author.objects.get(id=1)
#   update3.save()
# Assign the second author to the first 3 books
#   update4=Book.objects.get(id=3)
#   update4.Author.objects.get(id=2)
#   update4.save()
# Assign the third author to the first 4 books
#   update5=Book.objects.get(id=4)
#   update5.Author.objects.get(id=3)
#   update5.save()
# Assign the fourth author to the first 5 books (or in other words, all the books)
# For the 3rd book, retrieve all the authors
    #Book.objects.get(id=3).authors
# For the 3rd book, remove the first author
    #delete_book=Book.objects.get(id=3)
    #delete_author=Author.objects.get(id=1)
    #delete_author=books.delete(delete_book)
# For the 2nd book, add the 5th author as one of the authors
    #this_book=Book.objects.get(id=2)
    #this_author=Author.objects.get(id=5)
    #this_author=books.add(this_book)
# Find all the books that the 3rd author is part of
    #this_author=Author.objects.get(id=3)
    #books=Book.objects.filter(authors=this_author)
# Find all the books that the 2nd author is part of
    #this_author=Author.objects.get(id=2)
    #books=Book.objects.filter(authors=this_author)


