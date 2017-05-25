from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login,authenticate,logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView,DetailView,CreateView
from .forms import SignupForm,CreatePostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        # this is optional, you can just use UserCreationForm instead
        form = SignupForm(request.POST)
        if form.is_valid():
            # user created
            form.save()
            # get data and pass it to authenticate() to login right after registered
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request,'signup.html',{'form':form})

#basicly using the same logic as signup view,the main different here is using django built-in AuthenticationForm
def login_view(request):
    if request.user.is_authenticated():
        return HttpResponse('{} Already Logged In'.format(request.user))

    if request.method == 'POST':
        loginform = AuthenticationForm(data=request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/')
    else:
        loginform = AuthenticationForm()
    return render(request,'login.html',{'loginform':loginform})



# simple logout view
@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('basic_app:index'))


class PostCreateView(LoginRequiredMixin,CreateView):
    form_class = CreatePostForm
    template_name = 'post_form.html'
    login_url = 'basic_app:login'

    # https://stackoverflow.com/questions/22238663/pass-current-user-to-initial-for-createview-in-django
    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form.instance)
        return super(PostCreateView, self).form_valid(form)


class PostListView(ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'post_detail.html'
    model = Post
    context_object_name = 'post'