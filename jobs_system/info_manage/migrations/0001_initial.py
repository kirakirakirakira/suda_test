# Generated by Django 4.2.5 on 2023-11-29 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
            ],
            options={
                'verbose_name': '类别信息',
                'verbose_name_plural': '类别信息',
                'db_table': 'db_category',
            },
        ),
        migrations.CreateModel(
            name='JobModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='名称')),
                ('money', models.CharField(max_length=100, verbose_name='薪资范围')),
                ('edu_level', models.CharField(max_length=100, verbose_name='学历')),
                ('image', models.ImageField(default='default_job_img.png', max_length=300, upload_to='', verbose_name='图片')),
                ('content', models.TextField(verbose_name='介绍')),
                ('number', models.IntegerField(default=1, verbose_name='岗位数量')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('view_number', models.IntegerField(default=0, verbose_name='浏览量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.categorymodel', verbose_name='所属分类')),
            ],
            options={
                'verbose_name': '职位信息',
                'verbose_name_plural': '职位信息',
                'db_table': 'db_job',
            },
        ),
        migrations.CreateModel(
            name='UserInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('phone', models.CharField(max_length=100, verbose_name='手机号')),
                ('edu_level', models.CharField(default='', max_length=100, verbose_name='学历')),
                ('major', models.CharField(default='', max_length=100, verbose_name='专业')),
                ('age', models.IntegerField(default=0, verbose_name='年龄')),
                ('content', models.TextField(default='', verbose_name='介绍')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='加入时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'db_user_info',
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, '简历未通过'), (1, '简历通过'), (2, '面试通过'), (3, '面试未通过'), (4, '已发送录用通知'), (5, '已发送简历')], default=5, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='投递时间')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.jobmodel', verbose_name='所属职位')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.userinfomodel', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '投递信息',
                'verbose_name_plural': '投递信息',
                'db_table': 'db_order',
            },
        ),
        migrations.CreateModel(
            name='MarkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=5, verbose_name='评分')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.jobmodel', verbose_name='所属职位')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.userinfomodel', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '评分信息',
                'verbose_name_plural': '评分信息',
                'db_table': 'db_mark',
            },
        ),
        migrations.CreateModel(
            name='HotModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.jobmodel', verbose_name='热门职位')),
            ],
            options={
                'verbose_name': '热门商品',
                'verbose_name_plural': '热门商品',
                'db_table': 'db_hot',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.jobmodel', verbose_name='所属职位')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.userinfomodel', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '评论信息',
                'verbose_name_plural': '评论信息',
                'db_table': 'db_comment',
            },
        ),
        migrations.CreateModel(
            name='CollectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='投递时间')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.jobmodel', verbose_name='所属职位')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info_manage.userinfomodel', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': '收藏信息',
                'verbose_name_plural': '收藏信息',
                'db_table': 'db_collect',
            },
        ),
    ]
