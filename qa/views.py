from django.shortcuts import render
from forms import MessageForm
from .forms import ProductForm, question_form
from qa.models import Question
from django.db import connection #to enable django db connection to database
import unicodedata #to convert unicode to string

def ask_question(request):
    qa_form = question_form()
    question = request.POST.get('question')
    print("Question is : {0}".format(question))

    if request.method == 'POST':
        qa_form = question_form(request.POST)
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
            question = request.POST.get('question')
            str_question = unicodedata.normalize('NFKD', question).encode('ascii','ignore')
            #print("The question is : {0}".format(str_question))
            #str_question = unicodedata.normalize('NFKD', question).encode('ascii','ignore')
            print(type(str_question))
            #print ("The type is {0}: ".format(type(str_question)))
            result = decision(str_question)
            context = {
                'title' : 'Intelligent Database Interface',
                'answer':result #question #result
            }
        else:
            print(qa_form.errors)

    #request not post, but get
    else:
        context = {
            'title' : 'Intelligent Database Interface',
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
        manager_question()
        print "director"
    elif asked_question.lower() in [x.lower() for x in director_question]:
        print 'manager'
    elif asked_question.lower() in [x.lower() for x in number_of_staff]:
        print 'number of staff'
    elif asked_question.lower() in [x.lower() for x in products_count]:
        product_question()
        print 'product count'

def manager_question():
    result = 'you are looking for manager'
    return result

def director_question():
    result = 'director question'

def number_of_staff():
    result = 'number_of_staff'

def products_question():
    result = 'products_count'

def product_create_view(request):
    context = {}
    return render(request, 'qa/product_create.html', context)

"""def product_create_view(request):
    #print(request.POST)
    #print(request.GET)
    if request.method == "POST":
        my_new_title = request.POST.get('title')
        print(my_new_title)
        #Product.objects.create(title = my_new_title)
    context = {}
    return render(request, 'qa/product_create.html', context)

"""
"""def product_create_view(request):
    form = ProductForm(request.POST or None)
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
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            sub_form.save()
    else:
        print("Hello now")
        #message_form = MessageForm()

    return render(request, 'qa/index.html', {'form': MessageForm(), 'title':"Intelligent Interface"})
"""
