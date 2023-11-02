from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
from django.db.models.aggregates import Sum
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

#Create your views here.
def adminindex1(request):
    return render(request,'admin/adminpanel.html')

def addcategoryview(request):
    if request.method == 'POST':
        cat_name=request.POST.get('cat_name')
        cat_des=request.POST.get('cat_des')
        cat_img=request.FILES['cat_img']
        data=Category(cat_name=cat_name,cat_img=cat_img,cat_des=cat_des)
        data.save()

    return redirect('adminindex1')

def addcategory1(request):
    return render(request,'admin/addcategory.html')

def producttable1(request):
    data=Product.objects.all()
    return render(request,'admin/producttable.html',{'data':data})

def carttable1(request):
    data=Bill.objects.all()
    return render(request,'admin/carttable.html',{'data':data})

def contacttable1(request):
    data=Contact.objects.all()
    return render(request,'admin/contacttable.html',{'data':data})

def categorytable1(request):
    data=Category.objects.all()
    return render(request,'admin/categorytable.html',{'data':data})

def addproduct1(request):
    data=Category.objects.all()
    return render(request,'admin/addproduct.html',{'data':data})

def addproductview(request):
    if request.method == 'POST':
        pro_name=request.POST.get('pro_name')
        pro_cat=request.POST.get('pro_cat')
        pro_size=request.POST.get('pro_size')
        pro_price=request.POST.get('pro_price')
        pro_img=request.FILES['pro_img']
        data=Product(pro_name=pro_name,pro_price=pro_price,pro_cat=pro_cat,pro_size=pro_size,pro_img=pro_img)
        data.save()

    return redirect('adminindex1')

def proedit(request,eid):
    data1=Product.objects.filter(id=eid)
    data2=Category.objects.all()

    return render(request,'admin/editproduct.html',{'data1':data1,'data2':data2})

def proupdate(request,uid):
   if request.method == 'POST':
    pro_name=request.POST.get('pro_name')
    pro_size=request.POST.get('pro_size')
    pro_cat=request.POST.get('pro_cat')
    pro_price=request.POST.get('pro_price')
    try:
        pro_img = request.FILES['pro_img']
        fs = FileSystemStorage() 
        file = fs.save(pro_img.name, pro_img)
    except MultiValueDictKeyError :
        file=Product.objects.get(id=uid).pro_img
    data=Product.objects.filter(id=uid).update(pro_name=pro_name,pro_size=pro_size,pro_cat=pro_cat,pro_price=pro_price,pro_img=file)
   return redirect('producttable1')

def prodelete(request,did):
   data=Product.objects.filter(id=did)
   data.delete()
   return redirect('producttable1')

def catedit(request,eid):
    data=Category.objects.filter(id=eid)

    return render(request,'admin/editcategory.html',{'data':data})

def catupdate(request,uid):
   if request.method == 'POST':
    cat_name=request.POST.get('cat_name')
    cat_des=request.POST.get('cat_des')
    try:
        cat_img = request.FILES['cat_img']
        fs = FileSystemStorage() 
        file = fs.save(cat_img.name, cat_img)
    except MultiValueDictKeyError :
        file=Category.objects.get(id=uid).cat_img
    data=Category.objects.filter(id=uid).update(cat_name=cat_name,cat_des=cat_des,cat_img=file)
   return redirect('categorytable1')

def catdelete(request,did):
   data=Category.objects.filter(id=did)
   data.delete()
   return redirect('categorytable1')

def login1(request):
    return render(request,'login/login.html')

def register1(request):
    return render(request,'login/register.html')

def registerview(request):
    if request.method == 'POST':
       username1=request.POST.get('username')
       password1=request.POST.get('password')
       phone1=request.POST.get('phone')
       email1=request.POST.get('emailid')
       if User1.objects.filter(username1=username1).exists():
            return render(request,'login/register.html',{'msg1':'User already exisists'})
       else:
            data=User1(username1=username1,password1=password1,phone1=phone1,email1=email1)
            data.save()
          
    return redirect('login1')

def loginview(request):
    if request.method == 'POST':
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        if User.objects.filter(username__contains=username1).exists():
            user=authenticate(username=username1,password=password1)
            if user is not None:
                login(request,user)
                print(user)
                request.session['username1']=username1
                request.session['password1']=password1
                return redirect('adminindex1')
        elif User1.objects.filter(username1=username1,password1=password1).exists():
            data=User1.objects.filter(username1=username1,password1=password1).values('id','phone1','email1').first()
            request.session['id']=data['id']
            request.session['phone']=data['phone1']
            request.session['email']=data['email1']
            request.session['username']=username1
            request.session['password']=password1
            return render(request,'user/userindex.html')
        
    return render(request,'login/login.html',{'msg2':'Invalid username or password'})

def logout(request):
    del request.session['username']
    del request.session['password']
    del request.session['id']
    del request.session['phone']
    del request.session['email']
    return redirect('login1')
        
def usermain(request):
    u=request.session.get('id')
    count=Cart.objects.filter(userid=u,status=0).count()
    return render(request,'user/userindex.html',{'count':count})

def about(request):
    u=request.session.get('id')
    count=Cart.objects.filter(userid=u,status=0).count()
    return render(request,'user/aboutus.html',{'count':count})

def shop(request,category):
    u=request.session.get('id')
    count=Cart.objects.filter(userid=u,status=0).count()
    data1=Category.objects.all()
    if request.method == 'POST':
       search=request.POST.get('search')
       data=Product.objects.filter(pro_name=search)
    elif category == "all":
       data=Product.objects.all()
    else:
        data=Product.objects.filter(pro_cat=category)
    return render(request,'user/shop.html',{'data':data,'data1':data1,'count':count})

def productdetails(request,product_id):
    u=request.session.get('id')
    count=Cart.objects.filter(userid=u,status=0).count()
    datas=Product.objects.filter(id=product_id)
    return render(request,'user/viewdetails.html',{'datas':datas,'count':count})



def cart1(request):
    u=request.session.get('id')
    data=Cart.objects.filter(userid=u,status=0)
    return render(request,'user/cart.html',{'data':data})


def cartview(request,cid):
    if 'id' in request.session:
        total=request.POST.get('total')
        quantity=request.POST.get('quantity')
        userid=request.POST.get('id')
        data=Cart(productid=Product.objects.get(id=cid),quantity=quantity,total=total,userid=User1.objects.get(id=userid),status=0)
        data.save()
        return redirect('cart1')
    
@csrf_exempt
def cartupdate(request):
    if request.method == 'POST':
        cartid=request.POST.get('pid')
        q = request.POST.get('qty')
        print(q)
        p = request.POST.get('price')
        tot = float(q)*float(p)
        print(tot)
        Cart.objects.filter(id=cartid).update(total=tot,quantity=q)
    return HttpResponse()

def cartdelete(request,cdid):
    data=Cart.objects.filter(id=cdid)
    data.delete()
    return redirect('cart1')

def checkout(request):
    u=request.session.get('id')
    data=Cart.objects.filter(userid=u,status=0)
    total=Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    count=Cart.objects.filter(userid=u,status=0).count()
    return render(request,'user/checkout.html',{'data':data,'total':total,'count':count})

def checkoutview(request):
    if request.method == 'POST':
        Fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('emailid')
        mobile=request.POST.get('mobile')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        u=request.session.get('id')
        order=Cart.objects.filter(userid=u,status=0)
        for i in order:
            data=Bill(cartid=Cart.objects.get(id=i.id),Fname=Fname,Lname=lname,email=email,mobile=mobile,address1=address1,address2=address2,city=city,state=state,zip=zip)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
        return redirect('usermain1')

def contactus(request):
    u=request.session.get('id')
    count=Cart.objects.filter(userid=u,status=0).count()
    return render(request,'user/contact.html',{'count':count})

def contactview(request):
    if request.method == 'POST':
        name=request.POST.get('username')
        emailid=request.POST.get('emailid')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        data=Contact(name=name,emailid=emailid,subject=subject,message=message)
        data.save()

    return redirect('contact1')

def checkdelete(request,did):
    data=Bill.objects.filter(id=did)
    data.delete()
    return redirect('carttable1')
        

     



        
    





