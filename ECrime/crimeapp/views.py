from django.shortcuts import render, redirect
from.models import reg_tbl,crime_tbl,miss_tbl,report_tbl
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from.forms import EcrimeForm

# Create your views here.
def index(request):
    return render(request,"index.html")
def home(request):
    return render(request,"home.html")

def reg (request):
    if request.method=='POST':
        fnm = request.POST.get('fn')
        lnm = request.POST.get('ln')
        mob = request.POST.get('mb')
        em1 = request.POST.get('em')
        psw = request.POST.get('ps')
        obj =reg_tbl.objects.create(fn=fnm,lm=lnm,mb=mob,em=em1,ps=psw)
        obj.save()
        if obj:
            return render(request,"log.html")
        else:
            return render(request,"reg.html")
    else: 
        return render(request,"reg.html")
def log (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        obj =reg_tbl.objects.filter(em=username,ps=password)
        if obj:
            request.session['eml']=username
            request.session['psa']=password
            return render(request,"home.html")
        else:
            # Invalid login credentials
            error_message = "Invalid username or password."
            return render(request, "log.html", {'error_message': error_message})
    else:
        # Display login form
        return render(request, "log.html")
def userupde(request):
        obj =reg_tbl.objects.all()
        return render(request,"userupde.html",{"data":obj})
def edit(request):
        idno=request.GET.get('idn')
        obj=reg_tbl.objects.filter(id=idno)
        return render(request,"userupde2.html",{"data":obj})
def update(request):
    if request.method=='POST':
        idn=request.POST.get('idno')
        fnm = request.POST.get('fname')
        lnm = request.POST.get('lname')
        mob = request.POST.get('number')
        eml = request.POST.get('email')
        obj=reg_tbl.objects.get(id=idn)
        obj.fn=fnm
        obj.lm=lnm
        obj.mb=mob
        obj.em=eml
        obj.save()
        return redirect("/userupde")
    return render(request,"userupde2.html")
def delete(request):
    idno=request.GET.get('idn')
    obj=reg_tbl.objects.filter(id=idno)
    obj.delete()
    return redirect("/userupde")
def crime (request):
    if request.method=='POST':
        nm = request.POST.get('q1')
        pnm = request.POST.get('q2')
        age = request.POST.get('q3')
        add = request.POST.get('q4')
        gn = request.POST.get('q5')
        date = request.POST.get('q6')
        datereg = request.POST.get('q7')
        comp = request.POST.get('q8')
        section = request.POST.get('q9')
        comptype = request.POST.get('q10')

        obj =crime_tbl.objects.create(name=nm,pname=pnm,age=age,add=add,gen=gn,date=date,regdt=datereg,comp=comp,sec=section,comptyp=comptype)
        obj.save()
        if obj:
            return render(request,"cview.html")
        else:
            return render(request,"crime.html")
    else: 
        return render(request,"crime.html")
    
def missing (request):
    if request.method=='POST':
        fn= request.POST.get('fn')
        mob = request.POST.get('nmb')
        eml = request.POST.get('em')
        # als = request.POST.get('al')
        reltn = request.POST.get('rn')
        reltyp = request.POST.get('rlty')
        # addr = request.POST.get('add')
        gen = request.POST.get('gd')
        age = request.POST.get('age')
        yob = request.POST.get('yb')
        bb = request.POST.get('bb')
        bc = request.POST.get('bc')
        wt = request.POST.get('wt')
        ht = request.POST.get('ht')
        img = request.FILES.get('image')
        obj =miss_tbl.objects.create(fname=fn,nmb=mob,eml=eml,relnm=reltn,rlty=reltyp,gd=gen,age=age,yob=yob,bb=bb,bc=bc,wt=wt,ht=ht,img=img)
        obj.save()
        if obj:
            return render(request,"mview.html")
        else:
            return render(request,"missing.html")
    else: 
        return render(request,"missing.html")

def gallery(request):
    return render(request,"gallery.html")
def gallery1(request):
    return render(request,"gallery1.html")

def report(request):
    if request.method=='POST':
        loca = request.POST.get('loc')
        nm = request.POST.get('q2')
        bully = request.POST.get('bt')
        behaviour = request.POST.get('bb')
        repby = request.POST.get('q5')
        desc = request.POST.get('desc')
        pic = request.FILES.get('q7')
        comp = request.POST.get('q8')
        obj =report_tbl.objects.create(loc=loca,q2=nm,bt=bully,bb=behaviour,q5=repby,des=desc,q7=pic,q8=comp)
        obj.save()
        if obj:
            return redirect("/compview")
        else:
            return render(request,"regch.html")
    else: 
        return render(request,"regch.html")
    
def case(request):
    return render(request,"case.html")
def childcase(request):
    return render(request,"case1.html")
def wcase(request):
    return render(request,"case2.html")
def mcase(request):
    return render(request,"case4.html")
def rcase(request):
    return render(request,"case5.html")

def user_card(request):
    obj=crime_tbl.objects.all()
    return render(request,"cview.html",{"view":obj})

def mview (request):
    obj=miss_tbl.objects.all()
    return render(request,"mview.html",{"view":obj})

def compview (request):
    obj=report_tbl.objects.all()
    return render(request,"viewcomp.html",{"view":obj})

def status (request):
    obj=crime_tbl.objects.all()
    return render(request,"status_crime.html",{"view":obj})
def status1 (request):
    obj=miss_tbl.objects.all()
    return render(request,"status_miss.html",{"view":obj})
def status2 (request):
    obj=report_tbl.objects.all()
    return render(request,"status_report.html",{"view":obj})

def ecrime_mail(request):
    form=EcrimeForm()
    if request.method=='POST':
        form=EcrimeForm(request.POST)
        if form.is_valid():
           subject= form.cleaned_data.get('sub')
           message= form.cleaned_data.get('cont')
           recipient=form.cleaned_data.get('to')
           send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently=False)
           messages.success(request,'Successfully message send!.. ')
           return redirect('/ecrime_mail')
        return render(request,"sendmail.html",{'form':form})
def wanted (request):
    return render(request,"wanted.html")