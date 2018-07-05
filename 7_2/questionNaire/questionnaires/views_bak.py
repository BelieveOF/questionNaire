from django.shortcuts import render,HttpResponse,redirect
from .models import Questionnaires,Questions,Options
from django.contrib.auth.decorators import login_required
# Create your views here.
import pymysql

def index(request):
    return render(request,'user/index.html')

# 创建问卷
@login_required()
def createQuestionnaire(request):
    if request.method == 'GET':
        return render(request,'questionnaires/createQuestionnaire.html')
    elif request.method == "POST":
        title=request.POST.get('title')
        type=request.POST.get('naire_type')
        questionnaire=Questionnaires(title=title,questionnaire_type=type,creator_id=request.user.id)
        questionnaire.save()
        return redirect(MyLists)

# 所有问卷
def AllLists(request):
    user = request.user
    allLists=Questionnaires.objects.all()
    print(allLists)
    if user.is_authenticated:
        return render(request, 'questionnaires/AllLists.html',context={"myList":allLists})
    else:
        return render(request, 'questionnaires/error.html')

# 我的问卷
@login_required()
def MyLists(request):
    user=request.user
    if user.is_authenticated:
        myLists = Questionnaires.objects.filter(creator_id=request.user.id)
        return render(request,'questionnaires/MyLists.html',context={"myList":myLists})
    else:
        return render(request,'questionnaires/error.html')

def my_questions_options(request,pk):
    if request.method == 'GET':
        # user=request.questionnaires
        # print(user.pk)

        questions_dic = {}

        # 获取问卷标题
        questionnaire = Questionnaires.objects.filter(id=pk).first()
        print("问卷标题:",questionnaire.title)
        # 问卷创建者
        # print(questionnaire.creator_id)
        user = request.user
        # 当前用户ID
        print(user.id)
        # 增加点击量
        if user.id !=questionnaire.creator_id:
            # 问卷点击量
            print("点击量:", questionnaire.clicks)
            questionnaire.clicks += 1
            questionnaire.save()
        # 获取该问卷所有问题列表
        questions = Questions.objects.filter(title_id=pk)
        # print("所有问题对象:",questions)
        # 遍历问卷问题列表
        # for question_foo in questions:
        #     # 获取到一个问题的所有选项
        #     # print(question_foo.id)
        #     print(question_foo.question)
        #     options = Options.objects.filter(question_id=question_foo.id)
        #     options_dic={}
        #     for option_foo in options:
        #         print(option_foo.id, option_foo.option)
        #         options_dic[str(option_foo.id)]=option_foo.option
        #     # questions_dic[str(option_foo.id)]=option_foo.option
        #     # 存储问题ID以及选项
        #     # questions_dic['id']=str(question_foo.id)
        #     questions_dic[str(question_foo.id)+"."+question_foo.question]=options_dic
        # # print(options)

        data = {
            "id":pk,
            "title":questionnaire.title,
            "questions":questions,
        }
        # print(data)
        # print(data['questions'],type(data['questions']))
        # for question,options_foo in data['questions'].items():
        #     print(question,options_foo)
        #     for k,v in options_foo.items():
        #         print(k,v)
        return render(request, 'questionnaires/my_questions_options.html',context=data)
    else:pass
# 问卷详情(在所有界面显示)
def questions_options(request,pk):
    if request.method == 'GET':
        # user=request.questionnaires
        # print(user.pk)
        questions_dic = {}
        # 获取问卷标题
        questionnaire = Questionnaires.objects.filter(id=pk).first()
        # print("问卷标题:",questionnaire.title)
        # 问卷创建者
        # print(questionnaire.creator_id)
        user = request.user
        # 当前用户ID
        # print(user.id)
        # 增加点击量
        if user.id != questionnaire.creator_id:
            # 问卷点击量
            # print("点击量:", questionnaire.clicks)
            questionnaire.clicks += 1
            questionnaire.save()
        # 获取该问卷所有问题列表
        questions = Questions.objects.filter(title_id=pk)
        # print("所有问题对象:",questions)

        # # 遍历问卷问题列表
        # for question_foo in questions:
        #     # 获取到一个问题的所有选项
        #     # print(question_foo.id)
        #     print(question_foo.question)
        #     options = Options.objects.filter(question_id=question_foo.id)
        #     options_dic={}
        #     for option_foo in options:
        #         print(option_foo.id, option_foo.option)
        #         options_dic[str(option_foo.id)]=option_foo.option
        #     # questions_dic[str(option_foo.id)]=option_foo.option
        #     # 存储问题ID以及选项
        #     # questions_dic['id']=str(question_foo.id)
        #     questions_dic[str(question_foo.id)+"."+question_foo.question]=options_dic
        # # print(options)
        #
        # for question in questions:
        #     options = question.title
        #     break

        data = {
            "id":pk,
            "title":questionnaire.title,
            "questions":questions,
        }
        # print(data)
        # print(data['questions'],type(data['questions']))
        # for question,options_foo in data['questions'].items():
        #     print(question,options_foo)
        #     for k,v in options_foo.items():
        #         print(k,v)

        return render(request, 'questionnaires/questions_options.html',context=data)
    elif request.method == "POST":
        # 获取问题标题
        add_title = request.POST.get('add_title')
        # 获取该问卷ＩＤ
        questionnaire_id = request.POST.get('questionnaire_id')
        print(questionnaire_id)
        # num = request.POST.get('')
        add_options_dic = {}
        # for i in range(10):
        #     str1="option"+str(i)
        #     add_options['i']=request.POST.get(str1)
        add_options_dic['option1'] = request.POST.get('option1')
        add_options_dic['option2'] = request.POST.get('option2')
        print(add_options_dic['option1'])

        # 插入添加的问题
        add_question = Questions(question=add_title, title_id=questionnaire_id)
        add_question.save()
        # 　插入添加的选项
        add_question_id = Questions.objects.filter(question=add_title).first()
        print(add_question_id.id)
        add_options = Options(option=add_options_dic['option1'], question_id=add_question_id.id)
        add_options.save()
        add_options = Options(option=add_options_dic['option2'], question_id=add_question_id.id)
        add_options.save()

        # return redirect('questions_options/questionnaire_id/')
        return render(request, 'questionnaires/questions_options.html')


# 删除问卷
def naire_delete(request,pk):
    print(pk)
    question_naire = Questionnaires.objects.filter(id=pk)
    # print(question_naire.id)
    questions = Questions.objects.filter(title_id=pk)
    for question in questions:
        print(question.id,question.question)
        # 删除选项
        options = Options.objects.filter(question_id=question.id)
        for option in options:
            print(option.option)
        options.delete()
    questions.delete()
    question_naire.delete()
    # question
    return redirect(MyLists)



# 更改问卷
def naire_update(request,pk):
    return render(request,'questionnaires/error.html')

# 包含在问卷详情了
# # 创建问卷-问题
# def create_question(request):
#     if request.method == 'GET':
#         return render(request, 'questionnaires/questions_options.html')
#     elif request.method == "POST":
#         # 获取问题标题
#         add_title=request.POST.get('add_title')
#         # 获取该问卷ＩＤ
#         questionnaire_id=request.POST.get('questionnaire_id')
#         print(questionnaire_id)
#         # num = request.POST.get('')
#         add_options_dic={}
#         # for i in range(10):
#         #     str1="option"+str(i)
#         #     add_options['i']=request.POST.get(str1)
#         add_options_dic['option1']=request.POST.get('option1')
#         add_options_dic['option2']=request.POST.get('option2')
#         print(add_options_dic['option1'])
#
#         # 插入添加的问题
#         add_question=Questions(question=add_title,title_id=questionnaire_id)
#         add_question.save()
#         #　插入添加的选项
#         add_question_id=Questions.objects.filter(question=add_title).first()
#         print(add_question_id.id)
#         add_options=Options(option=add_options_dic['option1'],question_id=add_question_id.id)
#         add_options.save()
#         add_options=Options(option=add_options_dic['option2'],question_id=add_question_id.id)
#         add_options.save()
#
#
#         # return redirect('questions_options/questionnaire_id/')
#         return redirect(MyLists)
#         return render(request, 'questionnaires/questions_options.html',context={"questionnaire_id":questionnaire_id,"add_title":add_title,"add_options":add_options_dic})
#
