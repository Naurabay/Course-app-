

from django.db import models

class Category(models.Model):
    name = models.CharField('Category name', max_length=200, unique=True)
    imgpath = models.CharField( max_length=300 )

    def __str__(self):
        return self.name



class Course(models.Model):
    name = models.CharField('Course name', max_length=200)
    description = models.TextField('Description', max_length = 500)
    category = models.ForeignKey(Category, to_field="name", on_delete=models.CASCADE )# CASCADE - полное удаление данных пользователя
    logo = models.CharField('image logo', max_length=200)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField( max_length=100,blank=False)
    longitude = models.CharField( max_length=100,blank=False)
    address = models.CharField( max_length=200, blank=True)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE,  )

    def __str__(self):
        return self.address



class Contact(models.Model):
    CONTACTS= [
        (1, 'Phone'),
        (2, 'Email'),
        (3, 'VK'),
    ]

    contact_type = models.IntegerField(choices=CONTACTS) # IntegerField выпадающий список
    value = models.CharField(max_length=345)  #The longest e-mail in the world contains 345 characters
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='contacts' )


    def __str__(self):
        return self.value




