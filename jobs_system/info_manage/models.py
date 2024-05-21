from django.db import models


class UserInfoModel(models.Model):
    username = models.CharField(max_length=100, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    phone = models.CharField(max_length=100, verbose_name='手机号')
    edu_level = models.CharField(max_length=100, default='', verbose_name='学历')
    major = models.CharField(max_length=100, default='', verbose_name='专业')
    age = models.IntegerField(default=0, verbose_name='年龄')
    content = models.TextField(default='', verbose_name='介绍')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')

    class Meta:
        db_table = 'db_user_info'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserInfoModelProxy(UserInfoModel):
    class Meta:
        proxy = True
        verbose_name = "推荐求职者"
        verbose_name_plural = verbose_name


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')

    class Meta:
        db_table = 'db_category'
        verbose_name = '类别信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class JobModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    money = models.CharField(max_length=100, verbose_name='薪资范围')
    edu_level = models.CharField(max_length=100, verbose_name='学历')
    image = models.ImageField(upload_to='', default='default_job_img.png', max_length=300, verbose_name='图片')
    content = models.TextField(verbose_name='介绍')
    number = models.IntegerField(default=1, verbose_name='岗位数量')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    view_number = models.IntegerField(default=0, verbose_name='浏览量')

    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE, verbose_name='所属分类')

    class Meta:
        db_table = 'db_job'
        verbose_name = '职位信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


choices_list = [
    (0, '简历未通过'),
    (1, '简历通过'),
    (2, '面试通过'),
    (3, '面试未通过'),
    (4, '已发送录用通知'),
    (5, '已发送简历'),
]


class OrderModel(models.Model):
    job = models.ForeignKey('JobModel', on_delete=models.CASCADE, verbose_name='所属职位')
    user = models.ForeignKey('UserInfoModel', on_delete=models.CASCADE, verbose_name='所属用户')
    state = models.IntegerField(choices=choices_list, default=5, verbose_name='状态')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='投递时间')

    class Meta:
        db_table = 'db_order'
        verbose_name = '投递信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class CollectModel(models.Model):
    job = models.ForeignKey('JobModel', on_delete=models.CASCADE, verbose_name='所属职位')
    user = models.ForeignKey('UserInfoModel', on_delete=models.CASCADE, verbose_name='所属用户')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='投递时间')

    class Meta:
        db_table = 'db_collect'
        verbose_name = '收藏信息'
        verbose_name_plural = verbose_name


class HotModel(models.Model):
    job = models.ForeignKey('JobModel', on_delete=models.CASCADE, verbose_name='热门职位')

    class Meta:
        db_table = 'db_hot'
        verbose_name = '热门职位'
        verbose_name_plural = verbose_name


class CommentModel(models.Model):
    user = models.ForeignKey('UserInfoModel', on_delete=models.CASCADE, verbose_name='所属用户')
    job = models.ForeignKey('JobModel', on_delete=models.CASCADE, verbose_name='所属职位')
    content = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'db_comment'
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username


class MarkModel(models.Model):
    user = models.ForeignKey('UserInfoModel', on_delete=models.CASCADE, verbose_name='所属用户')
    item = models.ForeignKey('JobModel', on_delete=models.CASCADE, verbose_name='所属职位')
    score = models.IntegerField(default=5, verbose_name='评分')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'db_mark'
        verbose_name = '评分信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
