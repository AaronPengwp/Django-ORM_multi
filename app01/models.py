from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    price = models.IntegerField("价格") # 要入在开始位置
    pub_date = models.DateField()
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)

    authors = models.ManyToManyField("Author")

    def __str__(self):
        return self.name


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)

    def __str__(self):
        return self.name

#
# class Book_Author(models.Model):
#     book = models.ForeignKey("Book", on_delete=models.CASCADE)
#     author = models.ForeignKey("Author", on_delete=models.CASCADE)
