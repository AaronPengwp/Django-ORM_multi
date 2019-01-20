# Django-ORM_multi

在多表操作的基础上添加了对admin的界面的使用

多表操作（一对多）：
               #添加记录
               #publish_id=2
               Book.objects.create(name="linux运维",price=77,pub_date="2017-12-12",publish_id=2)
               

               #publish=object
               Book.objects.create(name="GO",price=23,pub_date="2017-05-12",publish=publish_obj)
               
               #查询记录（通过对象）
               
                     正向查询：
                     book_obj=Book.objects.get(name="python")   
                     pub_obj=book_obj.publish----》书籍对象对应的出版社对象
                     pub_obj.name
                     反向查询：
                     pub_obj = Publish.objects.filter(name="人民出版社")[0]
                     pub_obj.book_set.all().values("name","price")
                     
               #查询记录（filter values  双下划线__）
                     
                    #人民出版社出版过的书籍与价格
                    ret=Book.objects.filter(publish__name="人民出版社").values("name","price")
                    
                    #python这本书出版社的名字
                    ret2=Publish.objects.filter(book__name="python").values("name")
                    
                    #python这本书出版社的名字
                    ret3=Book.objects.filter(name="python").values("publish__name")
                    
                    #北京的出版社出版书的名字
                    ret4=Book.objects.filter(publish__city="北京").values("name")
                    
                    #2017年上半年出版过书的出版社的名字
                    ret5=Book.objects.filter(pub_date__lt="2017-07-01",pub_date__gt="2017-01-01").values("publish__name")
                    
                    
     多表操作（多对多）： 
                     
                    创建多对多的关系 author= models.ManyToManyField("Author")（推荐）
                    
                    
                    书籍对象它的所有关联作者  obj=book_obj.authors.all()
                            绑定多对多的关系  obj.add(*QuerySet)   
                                              obj.remove(author_obj)
                                              
                                              
                    如果想向第三张表插入值的方式绑定关系：  手动创建第三张表

                            # class Book_Author(models.Model):
                            #     book=models.ForeignKey("Book")
                            #     author=models.ForeignKey("Author")                    
                            Book_Author.objects.create(book_id=2,author_id=3)
                            
                    
                    掌握：通过 filter values (双下换线)进行多对多的关联查询（形式和一对多） 


-----------------------------------------------------------------
在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错：
TypeError: __init__() missing 1 required positional argument: 'on_delete'
举例说明：
user=models.OneToOneField(User)
owner=models.ForeignKey(UserProfile)
需要改成：
user=models.OneToOneField(User,on_delete=models.CASCADE) --在老版本这个参数（models.CASCADE）是默认值
owner=models.ForeignKey(UserProfile,on_delete=models.CASCADE) --在老版本这个参数（models.CASCADE）是默认值
参数说明：
on_delete有CASCADE、PROTECT、SET_NULL、SET_DEFAULT、SET()五个可选择的值
CASCADE：此值设置，是级联删除。
PROTECT：此值设置，是会报完整性错误。
SET_NULL：此值设置，会把外键设置为null，前提是允许为null。
SET_DEFAULT：此值设置，会把设置为外键的默认值。
SET()：此值设置，会调用外面的值，可以是一个函数。
一般情况下使用CASCADE就可以了。
