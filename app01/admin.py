from django.contrib import admin
from app01.models import *


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'pub_date')  # 设定默认显示 但是不支持多表的字段
    # list_per_page = 2  # 一页显示多少条内容
    search_fields = ('name', 'price', 'publish__name')  # 为数据表添加搜索功能
    list_filter = ('pub_date', 'publish')  # 添加快速过滤
    date_hierarchy = 'pub_date'  # 另外一种过滤日期 请注意，date_hierarchy接受的是* 字符串* ，而不是元组。因为只能对一个日期型字段进行层次划分。
    # ordering = ('price',)  # 按价格升序排序
    ordering = ('-price', "id") # 当价格有重复时再按id来排

    # `` 多对多字段``使用filter_horizontal。 这比多选框好用多了。 你可以在多个字段上使用filter_horizontal，
    # 只需在这个元组中指定每个字段的名字。
    #
    # ModelAdmin类还支持filter_vertical选项。 它像filter_horizontal那样工作，除了控件都是垂直排列，而不是水平排列的。
    # 至于使用哪个，只是个人喜好问题。
    #
    # filter_horizontal和filter_vertical选项只能用在多对多字段上, 而不能用于ForeignKey字段。 默认地，管理工具使用
    # `` 下拉框`` 来展现`` 外键`` 字段。但是，正如`` 多对多字段`` 那样，有时候你不想忍受因装载并显示这些选项而产生的大量开销。
    # 例如，我们的book数据库膨胀到拥有数千条publishers的记录，以致于book的添加页面装载时间较久，因为它必须把每一个publishe都装载并显示在
    # `` 下拉框``中。
    #
    # 解决这个问题的办法是使用`` raw_id_fields``选项。它是一个包含外键字段名称的元组，它包含的字段将被展现成
    # `` 文本框`` ，而不再是 `` 下拉框`` 。
    filter_horizontal = ('authors',)  # 多表操作时垂直显示
    # raw_id_fields = ('publisher',)


admin.site.register(Book, BookAdmin)  # 要把定制的类放在后面
admin.site.register(Publish)
admin.site.register(Author)
