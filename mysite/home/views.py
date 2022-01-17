from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,UpdateProfile,UpdateUser
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login as login_process,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'tài khoản đã được tạo thành công')
            return redirect('login')
    else: 
        form =RegisterForm()
    return render(request,'register.html',{'form':form})

def login(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login_process(request,user)
            return redirect('home')
        else:
            messages.info(request,'tai khoan hoac mat khau khong dung ')
    context = {}
    return render(request,'login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')
def home(request):
    return render(request,'home.html')
def homepage(request):
    return render(request,'homepage.html')



def postpage(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'post.html',context)


class PostListView(ListView):
    model = Post
    template_name = 'post.html' 
    context_object_name = 'posts'
    ordering = ['-dated_posted']        

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'object'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['tittle','content']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
            return reverse('post-detail',kwargs={'pk':self.object.pk})

class PostDeletelView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/post/'
    template_name = 'post_confirm_delte.html'
    context_object_name = 'object'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    model = Post
    fields = ['tittle','content']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
            return reverse('post-detail',kwargs={'pk':self.object.pk})

@login_required(login_url='login') 
def profile(request):
    if request.method == 'POST':
        u_form = UpdateUser(request.POST,instance=request.user)
        p_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'tài khoản của bạn đã được update')
            return redirect('profile')     
    else:
        u_form = UpdateUser(instance=request.user)
        p_form = UpdateProfile(instance=request.user.profile)   
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'profile.html',context)