from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect as redirect
from django.views.generic import ListView, TemplateView, CreateView, DeleteView
from .models import Comment, User
from django.urls import reverse, reverse_lazy
from .forms import AccountForm
from argon2 import PasswordHasher

class loginView(View):
    def get(self, request):
        post_form = AccountForm()
        return render(request, 'login.html', {'form' : post_form})

    def post(self, request):
        post_form = AccountForm(request.POST)
        if post_form.is_valid():
            account = request.POST.get('account')
            password = request.POST.get('password')
            
        else :
            print("유효하지 않음")
            return render(request, 'login.html', {'form' : post_form})

        try:
            if(User.objects.filter(account=account).exists()):
                PasswordHasher().verify(User.objects.get(account=account).pw, password)
                print(account.id)
                request.session['account'] = account.id
                print("로그인 성공")
        except:
            print("비밀번호가 틀림")

        return render(request, 'create.html')

class RegisterView(View):
    def get(self, request):
        page_form = AccountForm()
        
        return render(request, 'login.html', {'form' : page_form})

    def post(self, request):
        page_form = AccountForm(request.POST)
        account = request.POST.get('account')
        password = PasswordHasher().hash(request.POST.get('password'))
        print(password)
        if(User.objects.filter(account=account).exists()):
            print("계정이 이미 존재함")
            return render(request, 'create.html')

        new_user = User(account=account, pw=password)
        new_user.save()

        print(User.objects.all())

        print(account, password)
        return render(request, 'create.html')




class ListView(ListView):
    model = Comment
    template_name = 'comment.html'
    context = Comment.objects.all()


class CreateView(CreateView):
    model = Comment
    fields = ['name', 'comment']
    template_name='comment.html'
    success_url = "/study"

    def post(self, request, *args, **kwargs):
        self.object = None
        print("post : ", self.get_object)
        return super().post(request, *args, **kwargs)

class DeleteStudy(DeleteView):
    model = Comment
    success_url="/study"
    template_name = "comment.html"
    # Comment.objects.filter(id=id_).delete()

