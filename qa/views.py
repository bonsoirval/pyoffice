from django.shortcuts import render
from forms import MessageForm
from .forms import ProductForm, question_form
from qa.models import Question
from django.db import connection #to enable django db connection to database
import unicodedata #to convert unicode to string

def ask_question(request):
    qa_form = question_form(request.GET or None)

    if request.method == 'GET':
        qa_form = question_form(request.GET)
        context = {
            'form' : qa_form
        }
        if qa_form.is_valid():
            answer = Question.objects.values_list('qa_answer_sql', flat=True)#get(id=1)
            cursor = connection.cursor()
            cursor.execute("SELECT qa_answer_sql FROM Qa_question where id=1")
            row = cursor.fetchone()
            #return row
            #print(qa_form.cleaned_data)
            #pass data to the form
            question = request.GET.get('question')
            str_question = unicodedata.normalize('NFKD', question).encode('ascii','ignore')
            #print("The question is : {0}".format(str_question))
            #str_question = unicodedata.normalize('NFKD', question).encode('ascii','ignore')
            #print(type(str_question))
            print ("The type is {0}: ".format(type(str_question)))
            result = decision(str_question)
            context = {
                'title' : 'Intelligent Database Interface',
                'question':question,
                'answer':result #question #result
            }
        else:
            print("form submission not valid")
            print(qa_form.errors)
            context = {
                'title' : 'Intelligent Database Interface',
                'question':question,
                'answer':'nothing',
            }

    #request not GET, but get
    else:
        context = {
            'title' : 'Intelligent Database Interface',
            'question':question,
            'answer':'nothing',
        }
    return render(request, 'qa/index.html', context)

def decision(asked_question):
    director_question = [
            'What is the name of the director',
            'What is the name of the director?',
            'who is your director',
            'who is your director?'
        ]

    manager_question = [
            'what is the name of the manager',
            'What is the name of the manager?',
            'who is your manager',
            'who is your manager?'
        ]
    number_of_staff = [
            'How many staff are there in the company?',
            'how many people are employed in this compnay?',
            'how many people work here?'
            'what number of people work in this firm?'
        ]
    products_count = [
            'Company product(s)?',
            'what the company produce?',
            'list company products'
    ]

    #print ("question type {0} ".format(type(asked_question)))
    #if asked_question.lower in [for question.lower() in manager_question]:
    if asked_question.lower() in [x.lower() for x in manager_question]:
        manager_answer = manager_question_function()
        return manager_answer

    elif asked_question.lower() in [x.lower() for x in director_question]:
        director_answer = director_question_function()
        print("director function ")
        return director_answer

    elif asked_question.lower() in [x.lower() for x in number_of_staff]:
        number_of_staff_answer = number_of_staff_function()
        return number_of_staff_answer

    elif asked_question.lower() in [x.lower() for x in products_count]:
        products_question_answer = products_question_function()
        return products_question_function

def manager_question_function():
    result = 'you are looking for manager'
    return result

def director_question_function():
    result = 'you are looking for director'
    return result

def number_of_staff_function():
    result = 'you are looking for the number of staff'
    return result

def products_question_function():
    result = 'you are looking for our products'
    return result

def product_create_view(request):
    context = {}
    return render(request, 'qa/product_create.html', context)

"""def product_create_view(request):
    #print(request.GET)
    #print(request.GET)
    if request.method == "GET":
        my_new_title = request.GET.get('title')
        print(my_new_title)
        #Product.objects.create(title = my_new_title)
    context = {}
    return render(request, 'qa/product_create.html', context)

"""
"""def product_create_view(request):
    form = ProductForm(request.GET or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form':form
    }
    return render(request, 'qa/product_create.html', context)
"""
def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'qa/index.html', {'form': MessageForm(), 'title':"Intelligent Database Interface"})

"""def ask_question(request):
    if request.method == 'GET':
        message_form = MessageForm(request.GET)
        if message_form.is_valid():
            sub_form.save()
    else:
        print("Hello now")
        #message_form = MessageForm()

    return render(request, 'qa/index.html', {'form': MessageForm(), 'title':"Intelligent Interface"})
"""
