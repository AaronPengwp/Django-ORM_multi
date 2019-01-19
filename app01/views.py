from django.shortcuts import render, HttpResponse
from app01.models import *
from django.db.models import Avg, Min, Sum, Max, Count
from django.db.models import Q, F


# Create your views here.

def index(request):
    return render(request, 'index.html')


def addbook(request):
    ############多表操作（一对多）###################
    # publish_id=2 添加数据
    # 方式一
    # Book.objects.create(name="Linux", price=77, pub_date="2017-3-12", publish_id=2)

    # 方式二
    # publish_obj=Publish.objects.get(name="人民出版社")
    # Book.objects.create(name="GO", price=23, pub_date="2017-05-12", publish=publish_obj)

    ############多表操作（多对多）###################
    # 通过对象的方式绑定关系

    # book_obj = Book.objects.get(id=3)
    #
    # print(book_obj.authors.all()) # <QuerySet [<Author: Lili>]>
    # print(type(book_obj.authors.all())) # <class 'django.db.models.query.QuerySet'>

    # author_obj = Author.objects.get(id=1)
    # print(author_obj.book_set.all())

    book_obj = Book.objects.get(id=3)
    # author_obj = Author.objects.get(id=4)
    # book_obj.authors.add(author_obj)
    # 为id=3添加所有作者，要是有重复的就不会再添加
    # author_objs = Author.objects.all()
    # book_obj.authors.add(*author_objs)

    # 把书id=3的作者为1的删掉
    # book_obj.authors.remove(1)
    # book_obj.authors.remove(*author_objs)

    # 如果想向第三张表插入值的方式绑定关系：  手动创建第三张表
    # Book_Author.objects.create(book_id=1,author_id=3)

    # obj = Book.objects.get(id=1)
    # print("===>",obj.book_author_set.all()[0].author)  # __str__已经修改 Alex
    # print(obj.book_author_set.all()[0].author.age)

    # Aaron出过的书籍名称及价格
    # ret = Book.objects.filter(book_author__author__name="aaron").values("name","price")
    # print(ret)

    # authors = models.ManyToManyField("Author")
    # ret = Book.objects.filter(authors__name="Aaron").values("name", "price", "authors__name")
    # print(ret)

    #.聚合查询aggregate(*args,**kwargs)
    # ret = Book.objects.all().aggregate(Avg("price"))
    # ret = Book.objects.aggregate(Sum("price"))
    # ret = Book.objects.filter(authors__name="Aaron").aggregate(Aaron_money=Sum("price"))
    # ret = Book.objects.filter(authors__name="Aaron").aggregate(Count("price"))
    #
    # print("===>", ret)

    # 分组查询annotate
    # 所有作者出过书的价格
    # ret = Book.objects.values("authors__name").annotate(Sum("price"))
    # print("===>", ret)

    #各个出版社出过书名的最低价格
    # ret = Publish.objects.values("name").annotate(Min("book__price"))
    # print("===>", ret)

    # b = Book.objects.get(name="GO", price=99)
    # print(b)

    # F查询
    # 所有书的价格加10
    # Book.objects.all().update(price = F("price")+10)

    # Q查询 实现与或非
    # ret = Book.objects.filter(price=109)
    # print(ret) # <QuerySet [<Book: python>, <Book: GO>]>

    # ret = Book.objects.filter(Q(price=109)&Q(name="GO"))
    # print(ret) # <QuerySet [<Book: GO>]>

    # ret = Book.objects.filter(~Q(name="GO"))
    # print(ret) # <QuerySet [<Book: GO>]>

    # ret = Book.objects.filter(name__contains="G")
    # print(ret) # <QuerySet [<Book: GO>]>

    # 关键字与F、Q混着用的时候，F、Q必须放在最前面
    # ret = Book.objects.filter(Q(name="GO"), price=109)
    # print(ret)

    # QuerySet 属于惰性求值，只有当你用的时候才执行SQL，不然不执行
    # ret=Book.objects.filter(price=109)

    # QuerySet 加入了缓存，两次for 只会执行一次sql语句
    # for i in ret:
    #     print(i.price)

    # for i in ret:
    #     print(i.price)




    # ret=Book.objects.filter(price=200)

    # for i in ret:
    #     print(i.price)

    # 因为有缓存，所以你重新改的时候要重新查询查询
    # Book.objects.all().update(price=200)
    # ret = Book.objects.filter(price=100)
    # for i in ret:
    #     print(i.price)

    # exists检查是否有数据，可以避免数据放入到QuerySet缓存
    # if ret.exists():
    #     print("ok")


    # 把查询结果结果变成一个生成器，
    # ret=ret.iterator()
    # print(ret)
    #
    # for i in ret:
    #     print(i.name)
    #
    # 没有打印，因为在上面iterator已经到头了
    # for i in ret:
    #     print(i.name)

    #当数据量很大的时候到最好用iterator, 但数据量不大而且重复使用就用缓存


    return HttpResponse("添加成功")


def update(request):
    return HttpResponse("更新成功")


def delete(request):
    return HttpResponse("删除成功")


def select(request):
    ############多表操作（一对多）###################
    # （通过对象）

    book_obj = Book.objects.get(name="python")
    # print("===>", book_obj.name)
    # print("===>", book_obj.pub_date)

    # #一对多：book_obj.publish--------一定是一个对象
    # print(book_obj.publish.name)
    # print(book_obj.publish.city)
    # print(book_obj.publish)  # 返回的是一个对象，因为对__str__返回值做了修改

    # 查询人民出版社出过的所有书籍名字和价格
    # 方式一：
    # pub_obj = Publish.objects.filter(name="人民出版社")[0]
    # pub_obj = pub_obj.book_set.all().values("name","price")
    # print("===>", pub_obj)

    # 方式二：
    # pub_obj = Publish.objects.filter(name="人民出版社")[0]
    # ret = Book.objects.filter(publish=pub_obj).values("name", "price")
    # print("===>", ret)

    # 方式三：(filter values  双下划线__）
    # pub_obj = Book.objects.filter(publish__name="人民出版社").values("name", "price")
    # print("===>", pub_obj)

    # python这本书出版社的名字
    # ret1 = Publish.objects.filter(book__name="python").values("name")
    # print(ret1)

    # ret2 = Book.objects.filter(name="python").values("publish__name")
    # print(ret2)

    # 北京的出版社出版书的名字
    # ret3 = Book.objects.filter(publish__city="北京").values("name")
    # print(ret3)

    # 2017年上半年出版过书的出版社的名字
    # ret4 = Book.objects.filter(pub_date__lt="2017-06-01", pub_date__gt="2017-01-01").values("publish__name")
    # print(ret4)

    ############多表操作（多对多）###################

    return HttpResponse("查询成功")
