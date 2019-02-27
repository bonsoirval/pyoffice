from django import forms
from .models import Product

class question_form(forms.Form):
    question = forms.CharField()
    answer = forms.CharField()



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


from crispy_forms.layout import Layout, ButtonHolder, Submit, Field
from crispy_forms.helper import FormHelper
from django.contrib.auth.views import LoginView

##-- copied for form processing --##
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class MessageForm(forms.Form):
    text_input = forms.CharField()

    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    answer = forms.CharField(
        widget = forms.Textarea(),

    )

    question = forms.CharField(
        widget = forms.Textarea(),

    )

    radio_buttons = forms.ChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', "Option two can is something else and selecting it will deselect option one")
        ),
        widget = forms.RadioSelect,
        initial = 'option_two',
    )


    checkboxes = forms.MultipleChoiceField(
        choices = (
            ('option_one', "Option one is this and that be sure to include why it's great"),
            ('option_two', 'Option two can also be checked and included in form results'),
            ('option_three', 'Option three can yes, you guessed it also be checked and included in form results')
        ),
        initial = 'option_one',
        widget = forms.CheckboxSelectMultiple,
        help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
    )

    appended_text = forms.CharField(
        help_text = "Here's more help text"
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    multicolon_select = forms.MultipleChoiceField(
        choices = (('1', 'Purchasing Department'), ('2', 'Marketing Department'), ('3', 'Administrative Department'), ('4', '4'), ('5', '5')),
    )

    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_action = 'ask_question'
    helper.layout = Layout(

    Div(
        #Div(Field('text_input',label="", placeholder="Type in your question"), css_class='span3'),
        Div(Field('question', label="", placeholder="Type in your question"), css_class='span3'),
        Div(Field('answer', label="", placeholder="Your answer shows here", readonly = 'yes',), css_class='span3', readonly='yes'),
    ),
        #Field('text_input', css_class='input-xlarge'),
        #Field('textarea', rows="3", css_class='input-xlarge'),
        #Field('textarea', rows="10", readonly = 'yes', css_class='input-xlarge'),
        #'radio_buttons',
        #Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
        #AppendedText('appended_text', '.00'),
        #PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
        #PrependedText('prepended_text_two', '@'),
        #'multicolon_select',

        FormActions(
            Submit('save_changes', 'Ask Question', css_class="btn-primary"),
            Submit('cancel', 'Reset'),
        )
    )
    helper.form_show_labels = False
    #helper.field['text_input'].label = False
