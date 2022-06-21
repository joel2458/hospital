from genericpath import exists
from multiprocessing import context
from django.core.mail import send_mail
from django.conf import settings
import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from healthApp.models import designation, doctor,department,appoinment
from django.contrib.auth.decorators import login_required




# Create your views here.
def homepage(request): 
    user=designation.objects.all()        
    return render(request,'homepage.html',{'user':user})

@login_required(login_url='user_login')
def adminhome(request):   
    if not request.user.is_staff: 
        return redirect('loginpage')  
    return render(request,'admin/adminhome.html')      
    

def doctorsignup(request):
    dep=department.objects.all()

    return render(request,'user/doctorsignup.html',{'dep':dep})

def loginpage(request):
    return render(request,'user/loginpage.html')

@login_required(login_url='user_login')
def load_add_department(request):
    return render(request,'admin/adddepartment.html')

@login_required(login_url='user_login')
def load_doctor_home(request):
    user=doctor.objects.filter(user=request.user)
    return render(request,'user/doctor_home.html',{'user':user})



def user_signup(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        cemail=request.POST['cemail']
        password=request.POST['password']
        cpass=request.POST['cpass']
        add=request.POST['add']
        specilisation=request.POST['spec']
      
        
        qua=request.POST['qua']
        phone=request.POST['phn']
      
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image="/static/image/defdoctor.jpg"
        print("hii")
        if password == cpass:
            if email == cemail:
                if User.objects.filter(username=uname).exists():
                    messages.info(request,"Username is allready exist")
                    return redirect('doctorsignup')
                else:
                    user=User.objects.create_user(
                        first_name=fname,
                        last_name=lname,
                        username=uname,
                        email=email,
                        password=password
                    )
                    user.save()
                    
                    print("save")
                    u=User.objects.get(id=user.id)
           
                    member=doctor(address=add,specilisation=specilisation,image=image,phone=phone,qualification=qua,user=u,)
                    member.save()
                    messages.info(request,"successfully Registered")
                    return redirect('loginpage')
            else:
                messages.info(request,"Email id not matching!!")
                return redirect('doctorsignup')
        else:
            messages.info(request,"password is not matching!!")
            return redirect('doctorsignup')
           
    else:
        return render(request,'user_signup.html')





def user_login(request): 
    try:
        if request.method == 'POST':
            try:
                username = request.POST['uname']
                password = request.POST['password']
                print("dddd")
                user = auth.authenticate(username=username, password=password)
                request.session["uid"] = user.id
                if user is not None:
                    if user.is_staff:
                        auth.login(request,user)
                        return redirect('adminhome') 
                    else:                     
                        auth.login(request, user)
                        messages.info(request, f'Welcome {username}')
                        return redirect('load_doctor_home')
                else:
                    messages.info(request, "invalid details")
                    return redirect('loginpage')
            except:
                messages.info(request, "invalid details1")
                return render('user/loginpage.html')
        else:
            messages.info(request, "invalid details2")
            return render('user/loginpage.html')
    except:
        messages.info(request, 'Invalid username or password')
        return render(request, 'user/loginpage.html')

@login_required(login_url='user_login')
def logout(request):
    request.session["uid"] = ""
    auth.logout(request)
    return redirect('homepage')

@login_required(login_url='user_login')
def add_department(request):
    if request.method=='POST':
        dep=request.POST['department']
        
        print("cat")
        crs=department()
        crs.department_name=dep
       
        crs.save()
        print("hii")
        return redirect('adminhome')

@login_required(login_url='user_login')

    
def show_doctor(request): 
    if not request.user.is_staff: 
        return redirect('loginpage')  
    user=doctor.objects.all()
   
  
    context={'user':user}
    return render(request,'admin/admin_show_doctors.html',context)


# def show_d(request): 


  
#     ctgs = request.GET.get('category')
#     imgs = department.objects.all()
#     if ctgs is not None:
#         img = designation.objects.filter(department_id=imgs.id)
    
    
#     context = {
#         'img':img,
#         'imgs':imgs,
#         }
#     return render(request,'admin_show_product.html',context)

    # if not request.user.is_staff: 
    #     return redirect('loginpage')  
    # user=designation.objects.all()
   
  
    # context={'user':user}
    # return render(request,'admin/admin_show_doctors.html',context)




# @login_required(login_url='user_login')
# def load_doctor_details(request,pk): 
#     doc=doctor.objects.get(id=pk)
#     doct=doctor.objects.all()
#     dep=department.objects.all()

#     return render(request,'admin/add_doctor_details.html',{'doc':doc,'dep':dep,'doct':doct})


@login_required(login_url='user_login')
def add_doctor_details(request,pk):
    doc=doctor.objects.get(id=pk)
    doct=doctor.objects.all()
    dep=department.objects.all()
 
    if request.method == 'POST': 
        
        depart = request.POST.get('department')
        dep = department.objects.get(id=depart)
        desig=request.POST['desig']
        desigdetails= designation(department=dep,designation=desig,doctor=doc)
        desigdetails.save()
        return redirect ('adminhome')

    
    
    return render(request,'admin/add_doctor_details.html',{'doc':doc,'dep':dep,'doct':doct})




# def homedep(request):
#     dep=department.objects.all()
#     if request.method == 'POST': 
        
#         depart = request.POST.get('department')
#         dep = department.objects.get(id=depart)
#         img=request.FILES['image']
#         images = request.FILES.getlist('images')
#         depimgs=department(department_image=img,department_images=images)
#         depimgs.save()
#         return redirect ('adminhome')

#     return render(request,'admin/add_homedep.html',{'dep':dep})


@login_required(login_url='user_login')
def showdoc(request,pk):
    doc=doctor.objects.get(id=pk)
    usr=designation.objects.filter(doctor_id=doc.id)
    context={'usr':usr,'doc':doc}
    return render(request,'admin/admin_show_doc.html',context)

def show_dep(request):
    dep=department.objects.all()
    return render(request,'admin/add_homedep.html',{'dep':dep})
    
def detail(request,pk):
    doc=department.objects.get(id=pk)
    usr=designation.objects.filter(department_id=doc.id)
    context={'usr':usr,'doc':doc}
    return render(request,'admin/show_department.html',context)



# def docdep(request):

#     ctgs = request.GET.get('department')
#     catgrs = designation.objects.all()
    
#     if ctgs is not None:
#         imgs = designation.objects.filter(department_id=catgrs.id)
#     catgrs = designation.objects.all()
    
#     context = {
#         'catgrs':catgrs,
#         'imgs':imgs,
#         }
#     return render(request,'admin/add_homedep.html',context)


# @login_required(login_url='user_login')
# def showdepdoc(request,pk):
#     doc=department.objects.get(id=pk)
#     depp=designation.objects.filter(department_id=doc.id)
#     context={'depp':depp}
#     return render(request,'admin/admin_show_doctors.html',context)


def delete_doctor(request,pk):
    udelete=doctor.objects.get(id=pk)
    if udelete.image is not None:
        if not udelete.image == "/static/image/defdoctor.jpg":
            os.remove(udelete.image.path)
        else:
            pass
    udelete.delete()
    return redirect('adminhome')



@login_required(login_url='user_login')
def doctor_profile(request,pk):
    
    
        # user=doctor.objects.filter(user=request.user)
        doc=doctor.objects.get(id=pk)
        dep=designation.objects.filter(doctor_id=doc.id)
      
        
        return render(request,'user/doctor_profile.html',{'dep':dep,})

# def doctor_dep(request,pk):
#     doc=doctor.objects.get(id=pk)
#     dep=designation.objects.filter(doctor_id=doc.id)
#     return render(request,'user/doctor_dep.html',{'dep':dep,})

def user_edit_profile(request):
    if request.method == 'POST':
        
      
        umember=doctor.objects.get(user=request.user)
        umember.user.first_name = request.POST.get('fname')
        umember.user.last_name = request.POST.get('lname')
        umember.user.username = request.POST.get('uname')
        umember.user.email = request.POST.get('email')
        print("helloww")
        umember.address = request.POST.get('add')
        umember.specilisation= request.POST.get('spec')
        umember.phone = request.POST.get('phn')
        umember.qualification = request.POST.get('qua')
        print("helloww")
        if request.FILES.get('file') is not None:
            if not umember.image == "/static/image/defdoctor.jpg":
                os.remove(umember.image.path)
                umember.image = request.FILES['file']
            else:
                umember.image = request.FILES['file']
        else:
            os.remove(umember.image.path)
            umember.image = "/static/image/defdoctor.jpg"
        
        umember.user.save()
        umember.save()
       
        return redirect('/')
    
    umember=doctor.objects.get(user=request.user)
        
    return render(request,'user/doctor_edit_profile.html',{'umember':umember})

# def load_patient_signup(request):
#     # dep=department.objects.all()

#     return render(request,'patient/patient_signup.html')
# def load_appoinment(request):
  
    

#     return render(request,'patient/appoinment.html')

def appoinments(request):
  
  
    dep=designation.objects.all()
 
    
    if request.method == 'POST':
       
        fname=request.POST['fname']
        add=request.POST['add']
        age=request.POST['age']
        gender=request.POST['gender']
        phone=request.POST['phn']
        blood=request.POST['blood']
        email=request.POST['email']
        depart = request.POST.get('department')
        doc = designation.objects.get(id=depart)
       
     
      
       
        print("hii")
        
           
        member=appoinment(name=fname,address=add,age=age,gender=gender,phone=phone,email=email,bloodgroup=blood,doctor=doc)
        member.save()
        messages.info(request,"successfully Registered")
        return redirect('/')
    #         else:
    #             messages.info(request,"Email id not matching!!")
    #             return redirect('patientsignup')
    # else:
    #         messages.info(request,"password is not matching!!")
    #         return redirect('patientsignup')
           
    
    return render(request,'patient/appoinment.html',{'dep':dep})


def patient_show_doc(request):
    dep=department.objects.all()
    return render(request,'admin/add_homedep.html',{'dep':dep})

# def show_appoinment(request,pk):
#     dop=doctor.objects.get(id=pk)
#     dep=appoinment.objects.filter(doctor_id=dop.id)
  
#     return render(request,'user/doctor_show_appoinment.html',{'dep':dep})


def sndmail(request,pk):
    dop=doctor.objects.get(id=pk)
    dep=appoinment.objects.filter(doctor_id=dop.id)
  
    if request.method == 'POST':
        subject = 'appoinment details'
        message = 'Dear user,\n today available.'
        recipient = request.POST["email"]
        print("ffffff")
        send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient])
        
        print("ggggg")
        return redirect('load_doctor_home')
    return render(request,'user/doctor_show_appoinment.html',{'dep':dep})


