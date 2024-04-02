from django.shortcuts import render, redirect
from .models import MarkModel, CommentModel, HotModel, CollectModel, OrderModel, JobModel, CategoryModel, UserInfoModel
from django.http import JsonResponse
import numpy as np


def index(request):
    hots = HotModel.objects.all()
    categories = CategoryModel.objects.all()
    context = {
        'hots': hots,
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        # 用户登录
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not (username or password):
            return JsonResponse({'code': 400, 'message': '缺少必传的参数'})
        user = UserInfoModel.objects.filter(username=username, password=password).first()
        if not user:
            return JsonResponse({'code': 400, 'message': '账号或密码错误'})
        request.session['login_in'] = True
        request.session['username'] = user.username
        request.session['user_id'] = user.id
        return JsonResponse({'code': 200})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        phone = request.POST.get('phone')
        if not (username or password1 or password2):
            return JsonResponse({'code': 400, 'message': '缺少必传的参数'})

        if password1 != password2:
            return JsonResponse({'code': 400, 'message': '两次输入的密码不一致！'})

        flag = UserInfoModel.objects.filter(username=username).first()
        if flag:
            return JsonResponse({'code': 400, 'message': '该用户名已存在'})
        UserInfoModel.objects.create(
            username=username,
            password=password1,
            phone=phone
        )
        return JsonResponse({'code': 200})


def logout(request):
    # 退出登录
    flag = request.session.clear()
    return redirect('/')


def job_detail(request, job_id):
    # 职位详情
    job = JobModel.objects.get(id=job_id)
    comments = CommentModel.objects.filter(job_id=job_id)
    user_id = request.session.get('user_id')
    if user_id:
        flag_mask = MarkModel.objects.filter(item_id=job_id, user_id=user_id).first()
    else:
        flag_mask = False

    job.view_number += 1
    job.save()
    context = {
        'job': job,
        'comments': comments,
        'flag_mask': flag_mask
    }
    return render(request, 'job_detail.html', context=context)


def job_list(request, category_id):
    # 职位列表
    jobs = JobModel.objects.filter(
        category_id=category_id
    )
    return render(request, 'job_list.html', {'jobs': jobs})


def add_order(request):
    # 投递简历
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'code': 400, 'message': '请先登录'})
    job_id = request.POST.get('job_id')
    flag = OrderModel.objects.filter(user_id=user_id, job_id=job_id).first()
    if flag:
        return JsonResponse({'code': 400, 'message': '您已投递该岗位，请勿重复投递!'})
    OrderModel.objects.create(
        user_id=user_id,
        job_id=job_id
    )
    return JsonResponse({'code': 200})


def add_collect(request):
    # 添加收藏
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'code': 400, 'message': '请先登录'})
    job_id = request.POST.get('job_id')
    flag = CollectModel.objects.filter(user_id=user_id, job_id=job_id).first()
    if flag:
        return JsonResponse({'code': 400, 'message': '您已收藏该岗位，请勿重复收藏!'})
    CollectModel.objects.create(
        user_id=user_id,
        job_id=job_id
    )
    return JsonResponse({'code': 200})


def add_comment(request):
    # 添加评论
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'code': 400, 'message': '请先登录'})
    content = request.POST.get('content')
    job_id = request.POST.get('job_id')
    if not content:
        return JsonResponse({'code': 400, 'message': '内容不能为空'})

    CommentModel.objects.create(
        user_id=user_id,
        content=content,
        job_id=job_id
    )
    return JsonResponse({'code': 200})


def input_score(request):
    # 用户对物品进行评分
    user_id = request.session.get('user_id')
    if not user_id:
        return JsonResponse({'code': 400, 'message': '请先登录'})
    score = int(request.POST.get('score'))
    item_id = request.POST.get('job_id')
    MarkModel.objects.create(
        item_id=item_id,
        score=score,
        user_id=user_id
    )
    return JsonResponse({'code': 200})


def my_collect(request):
    # 我的收藏
    user_id = request.session.get('user_id')
    collects = CollectModel.objects.filter(user_id=user_id)
    return render(request, 'my_collect.html', {'collects': collects})


def delete_collect(request):
    # 取消收藏
    collect_id = request.POST.get('collect_id')
    collect = CollectModel.objects.get(id=collect_id)
    collect.delete()
    return JsonResponse({'code': 200})


def my_order(request):
    # 我的投递信息
    user_id = request.session.get('user_id')
    orders = OrderModel.objects.filter(user_id=user_id)
    return render(request, 'my_order.html', {'orders': orders})


def my_info(request):
    user_id = request.session.get('user_id')
    if request.method == 'GET':
        # 个人信息界面
        info = UserInfoModel.objects.get(id=user_id)
        return render(request, 'my_info.html', {'info': info})
    else:
        # 更新个人信息
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone') or ''
        edu_level = request.POST.get('edu_level') or ''
        major = request.POST.get('major') or ''
        age = request.POST.get('age') or ''
        content = request.POST.get('content') or ''

        UserInfoModel.objects.filter(
            id=user_id
        ).update(
            username=username,
            password=password,
            phone=phone,
            edu_level=edu_level,
            major=major,
            age=age,
            content=content,
        )
        return JsonResponse({'code': 200})


def view_count(request):
    # 浏览量统计
    if request.method == 'GET':
        return render(request, 'view_count.html')
    else:
        jobs = JobModel.objects.all().order_by('-view_number')[:10]
        name_list = []
        count_list = []
        for job in jobs:
            name_list.append(job.name)
            count_list.append(job.view_number)
        return JsonResponse({'code': 200, 'name_list': name_list, 'count_list': count_list})


def calculate_cosine_similarity(user_ratings1, user_ratings2):
    # 将用户1的职位评分存入字典，键为职位ID，值为评分
    item_ratings1 = {rating.item_id: rating.score for rating in user_ratings1}
    # 将用户2的职位评分存入字典，键为职位ID，值为评分
    item_ratings2 = {rating.item_id: rating.score for rating in user_ratings2}

    # 找出两个用户共同评价过的职位
    common_items = set(item_ratings1.keys()) & set(item_ratings2.keys())

    if len(common_items) == 0:
        return 0.0  # 无共同评价的职位，相似度为0

    # 提取共同评价职位的评分，存入NumPy数组
    user1_scores = np.array([item_ratings1[item_id] for item_id in common_items])
    user2_scores = np.array([item_ratings2[item_id] for item_id in common_items])

    # 计算余弦相似度
    cosine_similarity = np.dot(user1_scores, user2_scores) / (
            np.linalg.norm(user1_scores) * np.linalg.norm(user2_scores))
    return cosine_similarity


def user_based_recommendation(request, user_id):
    try:
        # 获取目标用户对象
        target_user = UserInfoModel.objects.get(id=user_id)
    except UserInfoModel.DoesNotExist:
        return JsonResponse({'code': 400, 'message': '该用户不存在'})

    # 获取目标用户的职位评分记录
    target_user_ratings = MarkModel.objects.filter(user=target_user)

    # 用于存储推荐职位的字典
    recommended_items = {}

    # 遍历除目标用户外的所有其他用户
    for other_user in UserInfoModel.objects.exclude(pk=user_id):
        # 获取其他用户的职位评分记录
        other_user_ratings = MarkModel.objects.filter(user=other_user)

        # 计算目标用户与其他用户的相似度
        similarity = calculate_cosine_similarity(target_user_ratings, other_user_ratings)

        if similarity > 0:
            # 遍历其他用户评价的职位
            for item_rating in other_user_ratings:
                # 仅考虑目标用户未评价过的职位
                if item_rating.item not in target_user_ratings.values_list('item', flat=True):
                    if item_rating.item.id in recommended_items:
                        # 累积相似度加权的评分和相似度
                        recommended_items[item_rating.item.id]['score'] += similarity * item_rating.score
                        recommended_items[item_rating.item.id]['similarity'] += similarity
                    else:
                        # 创建推荐职位的记录
                        recommended_items[item_rating.item.id] = {'score': similarity * item_rating.score,
                                                                  'similarity': similarity}

    # 将推荐职位按照加权评分排序
    sorted_recommended_items = sorted(recommended_items.items(), key=lambda x: x[1]['score'], reverse=True)

    # 获取排名靠前的推荐职位的ID
    top_recommended_items = [item_id for item_id, _ in sorted_recommended_items[:5]]

    # 构建响应数据
    response_data = []
    for item_id in top_recommended_items:
        item = JobModel.objects.get(pk=item_id)
        similarity = recommended_items[item_id]['similarity']
        response_data.append({
            'name': item.name,
            'id': item.id,
            'image': item.image,
            'similarity': similarity,
        })
    context = {
        'response_data': response_data
    }
    return render(request, 'job_recommend.html', context=context)
