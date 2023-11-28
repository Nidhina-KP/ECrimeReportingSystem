from django.shortcuts import render,redirect
from.models import offreg_tbl,cmnt_tbl,news_tbl
from crimeapp.models import crime_tbl

# Create your views here.
def official (request):
    if request.method=='POST':
        unm = request.POST.get('un')
        em = request.POST.get('em')
        oid = request.POST.get('oid')
        psw = request.POST.get('psw')
        obj =offreg_tbl.objects.create(unm=unm,em=em,oid=oid,psw=psw)
        obj.save()
        if obj:
            return render(request,"details.html")
        else:
            return render(request,"officialreg.html")
    else: 
        return render(request,"officialreg.html")
def officiallog (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        obj =offreg_tbl.objects.filter(unm=username,psw=password)
        if obj:
            request.session['eml']=username
            request.session['psa']=password
            return render(request,"details.html")
        else:
            # Invalid login credentials
            error_message = "Invalid username or password."
            return render(request, "officialreg.html", {'error_message': error_message})
    else:
        # Display login form
        return render(request, "officialreg.html")
def dash (request):
    return render(request,"details.html")

def cmt (request):
    if request.method=='POST':
        title = request.POST.get('title')
        content = request.POST.get('text')
        
        obj =cmnt_tbl.objects.create(title=title,content=content)
        obj.save()
        if obj:
            return render(request,"details.html")
        else:
            return render(request,"officialreg.html")
    else: 
        return render(request,"officialreg.html")
def cmtview(request):
    obj=cmnt_tbl.objects.all()
    return render(request,"detailsview.html",{"view":obj})

def cmp(request):
    obj=crime_tbl.objects.all()
    return render(request,"viewcmp.html",{"view":obj})
def news(request):
    if request.method=='POST':
        title = request.POST.get('tl')
        content = request.POST.get('cnt')
        athr = request.POST.get('ar')
        img = request.FILES.get('im')
        obj =news_tbl.objects.create(title=title,content=content,athr=athr,img=img)
        obj.save()
        if obj:
            return render(request,"news_view.html")
        else:
            return render(request,"form.html")
    else: 
        return render(request,"form.html")
def news_view(request):
    obj=news_tbl.objects.all()
    return render(request,"article_list.html",{"view":obj})
def n_view (request):
    return render(request,"news_view.html")




# def jugde_view(request):
#     cid=request.GET.get('idn')
#     obj=crime_tbl.objects.filter(id=cid)
#     return render(request,"details2.html",{"view":obj})
# def update(request):
#     if request.method=="POST":
#         sts = request.POST.get('st')
#         obj=crime_tbl.objects.get(sts=sts)
#         obj.save()
#         return redirect("/cmp")
#     return render(request,"details2.html")

