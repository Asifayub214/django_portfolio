from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForms
from service.models import Service
from news.models import News
from django.core.paginator import Paginator
from contact.models import Contact






def homePage(request):
    # data = {
    #     'title' : 'Home Page',
    #     'bdata' : 'Hi Asif',
    #     'clist' : ['PHP','Java','Django'],
    #     'number' : [10, 20, 30, 40, 50],
    #     'student' : [
    #         {'Name' : 'Asif ayub', 'Phone' : '03446393942'},
    #         {'Name' : 'Atif', 'Phone' : '03406393999'}
    #     ]
    # }
    newsData = News.objects.all()
    
    servicesData = Service.objects.all().order_by('-service_title')[:3]  # - is used for desc order by
    if request.method == "GET":
        st = request.GET.get('servicename')
        if st !=None:
             servicesData = Service.objects.filter(service_title__icontains=st)      # __contains used for filter with any word or character
        

 
        data={
        'servicesData' : servicesData,
        'newsData' : newsData,
        
    }

    return render(request, "index.html", data)

def servicesData(request):
        
        ServiceData = Service.objects.all()
        paginator = Paginator(ServiceData, 2)   
        page_number = request.GET.get('page')
        ServiceDatafinal = paginator.get_page(page_number) 
 
        data={
        
        'ServiceDatafinal' : ServiceDatafinal
    }

        return render(request, "index.html", data)  

    

def newsDetails(request, slug):
    newsDetails=News.objects.get(news_slug=slug)
    data = {
        'newsDetails' : newsDetails
    }
    return render(request, "newsdetails.html",data)
    

def blog(request):
    return render(request, "blog.html")

def blog_details(request):
    return render(request, "blog_details.html")

def services_details(request):
    return render(request, "services_details.html")


def contact(request):
    msg = ''
    if request.method=="POST":
        empname=request.POST.get('name')
        empemail=request.POST.get('email')
        empphone=request.POST.get('phone')
        empwebsite=request.POST.get('website')
        empmessage=request.POST.get('message')
        en =Contact(name=empname,email=empemail,phone=empphone,website=empwebsite,message=empmessage)
        en.save()
        msg = 'Data Inserted'
       
    return render(request, "contact.html", {'n': msg})

def userform(request):
   
   output = ''
   fn = UserForms()
   data = {'form':fn}
   
   
   try: 
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        email = request.POST.get('email')
        phonenumber = request.POST.get('phoneNumber')
        print(firstname, lastname, email, phonenumber)
        
        data = {
            'firstname' : firstname,
            'lastname' : lastname,
            'email' : email,
            'phonenumber' : phonenumber,
            'output' : firstname + lastname + email + phonenumber,
            # 'form' : fn
        }
        
        # return HttpResponseRedirect('/blog/')         both are using for redirection a page
        return redirect('/blog/')
   except:
        pass
    
        return render(request, "userform.html",data)



def course(request):
    return HttpResponse("Welcome to django Course")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def calculator(request):
    c=''
    try:
        if request.method == 'POST':
            n1= eval(request.POST.get('num1'))
            n2= eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            
            if opr == '+':
                c=n1+n2
            elif opr== '-':
                c=n1-n2
            elif opr== '*':
                c=n1*n2
            elif opr=='/':
                c=n1/n2 
                
    except:
        c= "Invalid opr....."
    return render(request, "calculator.html",{'c': c}) 

    