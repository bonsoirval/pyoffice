from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Layout, ButtonHolder, Submit, Field
from crispy_forms.helper import FormHelper

class RegistrationForm(UserCreationForm):
    """class Meta:
        model = models.Post
        fields = ['title', 'text', 'tags', 'author', 'slug']
        """
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )
