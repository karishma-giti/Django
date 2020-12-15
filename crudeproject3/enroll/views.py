from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

class AddShowView(TemplateView):
    template_name='enroll/addandshow.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm=StudentRegistration()
        stud=User.objects.all()
        context = {'stu':stud,'form':fm}
        return context
    def post(self,request):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():#for validation data
            nm=fm.cleaned_data['name'] #for get data in database
            em=fm.cleaned_data['email']
            pm=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pm)
            reg.save()
            return HttpResponseRedirect('/enroll/') 

class UserDeleteView(RedirectView):
    url='/enroll/'
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


class UpdateUserData(View):
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
        return render(request,'enroll/updatestudent.html',{'form':fm})

    def post(self,request,id):
        pi = User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request,'enroll/updatestudent.html',{'form':fm})
        



# def addshow(request):
#     if request.method =="POST":
#         fm=StudentRegistration(request.POST)
#         if fm.is_valid():#for validation data
#             nm=fm.cleaned_data['name'] #for get data in database
#             em=fm.cleaned_data['email']
#             pm=fm.cleaned_data['password']
#             reg=User(name=nm,email=em,password=pm)
#             reg.save()
#             fm=StudentRegistration()
#     else:
#         fm=StudentRegistration()
#     stud=User.objects.all()#for get data
#     return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})

# def updatedata(request,id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         fm=StudentRegistration(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:
#         pi = User.objects.get(pk=id)
#         fm=StudentRegistration(instance=pi)
#     return render(request,'enroll/updatestudent.html',{'form':fm})


# Delete data
# def deletedata(request,id):
#     if request.method == 'POST':
#         pi = User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/enroll/') 
