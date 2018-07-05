from django.shortcuts import render, HttpResponse, redirect
from .models import Questionnaires, Questions, Options
from django.contrib.auth.decorators import login_required
# Create your views here.
import pymysql


def index(request):
    return render(request, 'user/index.html')


# 创建问卷
@login_required()
def createQuestionnaire(request):
    if request.method == 'GET':
        return render(request, 'questionnaires/createQuestionnaire.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        type = request.POST.get('naire_type')
        questionnaire = Questionnaires(title=title, questionnaire_type=type, creator_id=request.user.id)
        questionnaire.save()
        return redirect(MyLists)


# 所有问卷
def AllLists(request):
    user = request.user
    allLists = Questionnaires.objects.all()

    # print(allLists)
    if user.is_authenticated:
        return render(request, 'questionnaires/AllLists.html', context={"myList": allLists})
    else:
        return render(request, 'questionnaires/error.html')


# 我的问卷
@login_required()
def MyLists(request):
    user = request.user
    if user.is_authenticated:
        myLists = Questionnaires.objects.filter(creator_id=user.id)
        return render(request, 'questionnaires/MyLists.html', context={"myList": myLists})
    else:
        return render(request, 'questionnaires/error.html')


# 我的问卷详情 ----POST需要优化 （动态增加想数据库添加的option） 以及重定向到当前页面
def my_questions_options(request, pk):
    if request.method == 'GET':
        # 获取问卷标题
        questionnaire = Questionnaires.objects.filter(id=pk).first()
        print("问卷标题:", questionnaire.title)
        user = request.user
        # 当前用户ID
        # print(user.id)
        # 增加点击量
        if user.id != questionnaire.creator_id:
            # 问卷点击量
            print("点击量:", questionnaire.clicks)
            questionnaire.clicks += 1
            questionnaire.save()
        # 获取该问卷所有问题列表
        questions = Questions.objects.filter(questionnaire_id=pk)

        data = {
            "id": pk,
            "title": questionnaire.title,
            "questions": questions,
        }

        return render(request, 'questionnaires/my_questions_options.html', context=data)
    elif request.method=='POST':
        # 获取问题标题
        add_title = request.POST.get('add_title')
        # 获取该问卷ＩＤ
        questionnaire_id = request.POST.get('questionnaire_id')
        # print(questionnaire_id)
        # num = request.POST.get('')
        add_options_dic = {}
        # for i in range(10):
        #     str1="option"+str(i)
        #     add_options['i']=request.POST.get(str1)
        add_options_dic['option1'] = request.POST.get('option1')
        add_options_dic['option2'] = request.POST.get('option2')
        # print(add_options_dic['option1'])

        # 插入添加的问题
        add_question = Questions(name=add_title, questionnaire_id=questionnaire_id)
        add_question.save()
        # 　插入添加的选项
        add_question_id = Questions.objects.filter(name=add_title).first()
        # print(add_question_id.id)
        add_options = Options(name=add_options_dic['option1'], question_id=add_question_id.id)
        add_options.save()
        add_options = Options(name=add_options_dic['option2'], question_id=add_question_id.id)
        add_options.save()
        # return redirect('/questionnaires/my_questions_options/',args=pk)
        return redirect(MyLists)


# 问卷详情(在所有界面显示)
def questions_options(request, pk):
    if request.method == 'GET':
        questionnaire = Questionnaires.objects.filter(id=pk).first()
        user = request.user
        # 当前用户ID
        # 增加点击量
        if user.id != questionnaire.creator_id:
            # 问卷点击量
            # print("点击量:", questionnaire.clicks)
            questionnaire.clicks += 1
            questionnaire.save()
        # 获取该问卷所有问题列表
        questions = Questions.objects.filter(questionnaire_id=pk)
        data = {
            "id": pk,
            "title": questionnaire.title,
            "questions": questions,
        }
        return render(request, 'questionnaires/questions_options.html', context=data)
    elif request.method == "POST":
        pass



# 删除问卷   需要优化
def naire_delete(request, pk):
    print(pk)
    question_naire = Questionnaires.objects.filter(id=pk)
    # print(question_naire.id)
    questions = Questions.objects.filter(questionnaire_id=pk)
    for question in questions:
        # print(question.id, question.question)
        # 删除选项
        options = Options.objects.filter(question_id=question.id)
        # for option in options:
        #     print(option.option)
        #     pass
        options.delete()
    # 删除问题
    questions.delete()
    # 删除选项
    question_naire.delete()
    # question
    return redirect(MyLists)


# 更改问卷
def naire_update(request, pk):
    return render(request, 'questionnaires/error.html')
