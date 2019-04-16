from django.shortcuts import render
from forms import MessageForm
from .forms import ProductForm, question_form
from qa.models import Question, Manager_question, Manager, Director,\
Director_question, Product_list_question, Product_count_question, Product
from django.db import connection #to enable django db connection to database
from django.db.models import Count
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
            result = decision(str_question, request)
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

def decision(asked_question, request):

    #getting questions from database
    director_question   = Director_question.objects.values_list('director_question', flat=True)
    manager_question    = Manager_question.objects.values_list('manager_question', flat=True)#get(id=1)
    products_count      = Product_count_question.objects.values_list('product_count_question', flat=True)
    product_list        = Product_list_question.objects.values_list('product_list_question',flat=True) #all()
    print("Products list of available products : {0}".format(product_list))
    '''
    products_list = [
            'Company product(s)?',
            'what the company produce?',
            'list company products'
    ]
    '''

    number_of_staff = [
            'How many staff are there in the company?',
            'how many people are employed in this compnay?',
            'how many people work here?'
            'what number of people work in this firm?'
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
        products_question_answer = products_count_function(asked_question.lower())
        return products_question_answer
    elif asked_question.lower() in [x.lower() for x in product_list]:
        products_list_question_answer = products_list_function (asked_question.lower(), request)
        return products_list_question_answer
    else:
        error_message = 'I am not sure what you are looking for, so I made the '\
        'following suggestions for you: \n 1.{0} \n 2.{1} \n 3.{2} \n 4.{3} \n 5.{4}\n'.format(manager_question[0],director_question[0], number_of_staff[0], products_count[0], product_list[0])
        return error_message


def manager_question_function(asked_question):
    manager_title = Manager.objects.values_list('title', flat=True)#get(id=1)
    manager_name = Manager.objects.values_list('name', flat=True)
    result = "The company's manager is " + manager_title[0] + " " + manager_name[0]
    return result

def director_question_function(asked_question):
    director_title = Director.objects.values_list('title', flat=True)#get(id=1)
    director_name = Director.objects.values_list('name', flat=True)
    result = "The company's director is " + director_title[0] + " " + director_name[0]
    return result

def number_of_staff_function():
    result = 'you are looking for the number of staff'
    return result

def products_count_function(asked_question):
    print("Asked question is {0}".format(asked_question))
    product_count = Product.objects.all().count()
    product_count_statement = "The firm has {0} products in total".format(product_count)
    return product_count_statement

def products_list_function(asked_question, request):
    print("Asked question is {0} in products_list_function".format(asked_question))
    #product_list = request.POST.get('question')
    product_list = Product.objects.values_list('name', flat=True)
    #product_list = unicodedata.normalize('NFKD', unicode(product_list)).encode('ascii','ignore')
    product_list_statement = "The following are the products the company produces: {0} \
    ".format(str([str(product) for product in product_list]))
    return product_list_statement

def product_create_view(request):
    context = {}
    return render(request, 'qa/product_create.html', context)

def index(request):
    # This view is missing all form handling logic for simplicity of the example
    return render(request, 'qa/index.html', {'form': MessageForm(), 'title':"Intelligent Database Interface"})
