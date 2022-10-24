from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello World123!')

# def register_user(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             messages.success(request, ('Registration Successful'))
#             return redirect('login')
#     else:
#         form = UserCreationForm

#         context = {'form' : form}
#         return render(request, 'registration/register.html', context)