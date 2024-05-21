from django.contrib import admin
from django.utils.html import format_html

from .models import JobModel, CollectModel, OrderModel, UserInfoModel, CategoryModel, HotModel, CommentModel, MarkModel, \
    UserInfoModelProxy


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'phone', 'create_time')

class RecommendUserInfoAdmin(admin.ModelAdmin):
    list_display = ('username','edu_level','major','age', 'phone', 'create_time')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'money', 'edu_level')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="/image/{}" style="width:120px;height:70px;"/>'.format(obj.image))
        return ""

    image_tag.allow_tags = True
    image_tag.short_description = '照片'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'state')


class CollectAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'create_time')


class HotAdmin(admin.ModelAdmin):
    list_display = ('job',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'content', 'create_time')


class MarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'score', 'create_time')


admin.site.register(UserInfoModel, UserInfoAdmin)
admin.site.register(UserInfoModelProxy, RecommendUserInfoAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(JobModel, JobAdmin)
admin.site.register(OrderModel, OrderAdmin)
admin.site.register(CollectModel, CollectAdmin)
admin.site.register(HotModel, HotAdmin)
admin.site.register(CommentModel, CommentAdmin)
admin.site.register(MarkModel, MarkAdmin)
admin.site.site_header = '职位招聘管理系统后台'
