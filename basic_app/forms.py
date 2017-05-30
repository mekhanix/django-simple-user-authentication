from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  .models import Post
from tinymce.widgets import TinyMCE
# OPTIONAL
class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True, validators=[validators.EmailValidator()])
    vemail = forms.EmailField(required=True, validators=[validators.EmailValidator()], label='Email Confirmation')

    # https://stackoverflow.com/questions/13202845/removing-help-text-from-django-usercreateform
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        email = cleaned_data['email']
        vemail = cleaned_data['vemail']
        if email != vemail:
            raise forms.ValidationError("Email didn't Match")
        return cleaned_data

    class Meta:
        model = User
        fields = ('first_name','last_name','email','vemail','username','password1','password2')


class CreatePostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 400, 'rows': 400}))
    class Meta:
        model = Post
        fields = ('title','content')