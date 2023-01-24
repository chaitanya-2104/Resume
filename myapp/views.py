from django.shortcuts import render
from .forms import StudentForms,QualificationForms,QualificationForms1,QualificationForms2,QualificationForms3
# Create your views here.
from myapp.models import Forms
from polls.models import Qualification
from polls.models import Qualification1
from polls.models import Qualification2
from polls.models import Qualification3

from django.views import View

class HomeView(View):
    def get(self,request):
        form =StudentForms(prefix="sud")
        form1 =QualificationForms(prefix="Qu")
        form2 =QualificationForms1(prefix="Qp")
        form3 =QualificationForms2(prefix="Ql")
        form4 =QualificationForms3(prefix="Qiu")
       
        candidates =Forms.objects.all()
        #candidates1=Qualification.objects.all()
        return render(request,'myapp/home.html',{'candidates':candidates,'form':form,'form1':form1,'form2':form2,'form3':form3,'form4':form4})
    
    def post(self,request):
        if request.method=='POST':

            form = StudentForms(request.POST,request.FILES,prefix="sud")
            form1=QualificationForms(request.POST,prefix="Qu")
            form2=QualificationForms1(request.POST,prefix="Qp")
            form3=QualificationForms2(request.POST,prefix="Ql")
            form4=QualificationForms3(request.POST,prefix="Qiu")


            if form.is_valid():
                form.save()
                print("hello")
            if form2.is_valid():
                form1.save()
                print("hello1")
            
            if form1.is_valid():
                print("hello2")
                form2.save()
            else:
                print(form2.errors)
            if form3.is_valid():
                print("hello3")
                form3.save()
            if form4.is_valid():
                print("hello4")
                form4.save()
        


        return render(request,'myapp/home.html',{'form':form,'form1':form1,'form2':form2,'form3':form3,'form4':form4})
def Show(request):
    
    candidates =Forms.objects.all()
    candidates1=Qualification.objects.all() 
    candidates2=Qualification1.objects.all() 
    candidates3=Qualification2.objects.all() 
    candidates4=Qualification3.objects.all() 
    
    
    return render(request,'myapp/List.html',{'candidate1':candidates1,'candidates':candidates,'candidate2':candidates2,'candidate4':candidates4,'candidate4':candidates4})
class CandidatesView(View):
    def get(self,request,pk):
    
        candidates =Forms.objects.get(pk=pk)
        candidates1=Qualification.objects.get(pk=pk)
        candidates2=Qualification1.objects.get(pk=pk) 
        candidates3=Qualification2.objects.get(pk=pk)
        candidates4=Qualification3.objects.get(pk=pk)
      
    
        return render(request,'myapp/candidate.html',{'candidate1':candidates1,'candidates':candidates,'candidate2':candidates2,'candidate3':candidates3,'candidate4':candidates4})
   