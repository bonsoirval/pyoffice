from django.shortcuts import render
from forms import MessageForm
from .forms import ProductForm, question_form
from qa.models import Question, Manager_question, Manager, Director, Director_question
from django.db import connection #to enable django db connection to database
import unicodedata #to convert unicode to string

def ask_question(request):
    question = request.POST.get('question')
    qa_form = question_form()

    if request.method == 'POST':
        qa_form = question_form(request.POST)
        context = {
            'form' : qa_form
        }
        if qa_form.is_valid():
            #answer = Question.objects.values_list('qa_answer_sql', flat=True)#get(id=1)
            #cursor = connection.cursor()
            #cursor.execute("SELECT qa_answer_sql FROM Qa_question where id=1")
            #row = cursor.fetchone()
            #return row
            #print(qa_form.cleaned_data)
            #pass data to the form
            question = request.POST.get('question')
            str_question = unicodedata.normalize('NFKD', question).encode('ascii','ignore')
            #print("The question is : {0}".format(str_question))
            #str_question = unicodedata.normalize('NFKD', question).encode('ascii','ignore')
            #print(type(str_question))
            #print ("The type is {0}: ".format(type(str_question)))
            result = decision(str_question)
            context = {
                'title' : 'Intelligent Database Interface',
                'question':question,
                'answer':result #question #result
            }
        else:
            print(qa_form.errors)
            context = {
                'title' : 'Intelligent Database Interface',
                'question':question,
                'answer':'form submission not valid',
            }

    #request not POST, but get
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

    manager_question = Manager_question.objects.values_list('manager_question', flat=True)#get(id=1)

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

    #if asked_question.lower in [for question.lower() in manager_question]:
    if asked_question.lower() in [x.lower() for x in manager_question]:
        manager_answer = manager_question_function(asked_question.lower())
        return manager_answer

    elif asked_question.lower() in [x.lower() for x in director_question]:
        director_answer = director_question_function(asked_question.lower())
        return director_answer

    elif asked_question.lower() in [x.lower() for x in number_of_staff]:
        number_of_staff_answer = number_of_staff_function()
        return number_of_staff_answer

    elif asked_question.lower() in [x.lower() for x in products_count]:
        products_question_answer = products_question_function()
        return products_question_function

def manager_question_function(asked_question):
    manager_title = Manager.objects.values_list('title', flat=True)#get(id=1)
    manager_name = Manager.objects.values_list('name', flat=True)
    result = "The company's manager is " + manager_title[0] + " " + manager_name[0]
    return result

def director_question_function():
    director_title = Manager.objects.values_list('title', flat=True)#get(id=1)
    director_name = Manager.objects.values_list('name', flat=True)
    result = "The company's director is " + director_title[0] + " " + director_name[0]
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

def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'qa/index.html', {'form': MessageForm(), 'title':"Intelligent Database Interface"})
