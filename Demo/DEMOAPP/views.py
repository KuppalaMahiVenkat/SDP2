from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Post,Signup,log,Signup1,personalbanking2,personalbanking3,transaction,transaction1,electrical,mobile,mobile2,loanapp,insurance2,insurance
from .filters import UserFilter
from django.db import connection
from django.contrib.auth import logout as logouts

def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def aboutus(request):
    return render(request,'about us.html')
def service(request):
    return render(request,'card.html')
def invalid(request):
    return render(request,'invalid.html')

def exist(request):
    return render(request,'exist.html')
def access(request):
    return render(request,'access.html')
def banking(request):
    return render(request,'banking.html')
def personalbanking(request):
    return render(request,'form.html')
def transaction(request):
    return render(request, 'Transaction.html')
def mobilebanking(request):
    return render(request, 'mobile banking.html')
def electricalbill(request):
    return render(request, 'electricity bill.html')
def mobilerecharge(request):
    return render(request, 'mobile recharge.html')
def finance(request):
    return render(request, 'finance.html')
def loanapplication1(request):
    return render(request, 'loan application1.html')
def insurance(request):
    return render(request, 'insurance.html')
def plans(request):
    return render(request, 'plans.html')
def viewtrans(request):
    with connection.cursor() as cursor:
        a = request.session['cid']
        cursor.execute("SELECT * FROM personal3 WHERE cid = %s", (a,))
        b=cursor.fetchall()
    return render(request,"index.html",{'b':b})






def createpost(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('passw'):
            post = Post()
            post.username = request.POST.get('username')
            post.passw = request.POST.get('passw')
            post.save()
            return render(request, 'card.html')

    else:
        return render(request, 'login.html')

def signup1(request):
    if request.method == 'POST':
        if request.POST.get('an') and request.POST.get('mn') and request.POST.get('cid') and request.POST.get('cpass') :
            s=Signup1()
            s.an=request.POST.get('an')
            s.mn=request.POST.get('mn')
            s.cid=request.POST.get('cid')
            s.cpass= request.POST.get('cpass')
            s.save()
            return render(request, 'login.html')
    else:
        return render(request, 'home.html')

def login1(request):
    f=0
    if request.method == 'POST':
      if request.POST.get('cid') and request.POST.get('passw'):
            l=log()
            l.cid=request.POST.get('cid')
            l.passw=request.POST.get('passw')
            a=Signup1.objects.raw('SELECT cid ,cpass from signup4')
            for p in a:
                if p.cid == l.cid and  p.cpass == l.passw:
                    f=1
                    break
            if(f==1):
                l.save()
                request.session['cid']=l.cid
                request.session['eid'] = l.cid
                return render(request,'card.html')
            else:
                return render(request, 'invalid.html')
    else:
        return render(request, 'home.html')


def signup2(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('an') and request.POST.get('mn') and request.POST.get('cid') and request.POST.get('cpass'):
            s = Signup1()
            s.an = request.POST.get('an')
            s.mn = request.POST.get('mn')
            s.cid = request.POST.get('cid')
            s.cpass = request.POST.get('cpass')
            a=Signup1.objects.raw('SELECT cid,mn,an  from signup4')
            for p in a:
                if p.cid == s.cid or p.mn == s.mn or p.an == s.an:
                    f=1
                    break
            if(f==1):
                return render(request,'exist.html')
            else:
                s.save()
                return render(request, 'login.html')
    else:
        return render(request, 'home.html')

def logout(request):
    try:
        request.session['eid']
        del request.session['eid']
        return render(request,'home.html')
    except:
        logouts(request)
        return render(request, 'home.html')


def personal(request):
    if request.method == 'POST':
        if request.POST.get('cid') and request.POST.get('AN') and request.POST.get('CN') and request.POST.get('Amt') and request.POST.get('email'):
                p=personalbanking3()
                p.cid=request.session['cid']
                p.AN=request.POST.get('AN')
                p.CN=request.POST.get('CN')
                p.Amt=request.POST.get('Amt')
                p.email=request.POST.get('email')
                p.save()
                return render(request, 'card.html')
        else:
            return render(request,'fund.html')
    else:
        return render(request,'fund wrong.html')



def personal2(request):
    f=0
    if request.method == 'POST':
        if  request.POST.get('AN') and request.POST.get('CN') and request.POST.get('Amt') and request.POST.get('email'):
                p=personalbanking3()
                p.cid=request.session['cid']
                p.AN=request.POST.get('AN')
                p.CN=request.POST.get('CN')
                p.Amt=request.POST.get('Amt')
                p.email=request.POST.get('email')
                p.save()
                return render(request, 'fund.html')
        else:
            return render(request,'fund wrong.html')


def electricbill(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('cname')  and request.POST.get('Service') and request.POST.get('bill'):
            e=electrical()
            e.cname=request.POST.get('cname')
            e.cid=request.session['cid']
            e.Service=request.POST.get('Service')
            e.bill=request.POST.get('bill')
            e.save()
            return render(request, 'bill.html')
        else:
                return render(request, 'bill wrong.html')


def mobilebill(request):
    f=0
    if request.method == 'POST':
        if request.POST.get('mn')  and request.POST.get('sim') and request.POST.get('bill'):
            m=mobile()
            m.mn=request.POST.get('mn')
            m.cid=request.session['cid']
            m.sim=request.POST.get('sim')
            m.bill=request.POST.get('bill')
            m.save()
            return render(request, 'mobile.html')
        else:
            return render(request, 'mobile wrong.html')


def loan(request):
    if request.method == 'POST':
        if request.POST.get('amt') and request.POST.get('ir') and request.POST.get('months'):
            l=loanapp()
            l.cid=request.session['cid']
            l.amt=request.POST.get('amt')
            l.ir=request.POST.get('ir')
            l.months=request.POST.get('months')
            l.save()
            return render(request, 'sent.html')



def mobilebill2(request):
    if request.method == 'POST':
        if request.POST.get('sim') and request.POST.get('mn') and request.POST.get('bill'):
            m=mobile2()
            m.cid=request.session['cid']
            m.sim=request.POST.get('sim')
            m.mn = request.POST.get('mn')
            m.bill=request.POST.get('bill')
            m.save()
            return render(request, 'mobile.html')
        else:
            return render(request, 'mobile wrong.html')

def ins(request):
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('mn') and request.POST.get('address') and request.POST.get('occupation') and request.POST.get('loan'):
            i=insurance()
            i.cid = request.session['cid']
            i.fname = request.POST.get('fname')
            i.lname = request.POST.get('lname')
            i.email = request.POST.get('email')
            i.mn = request.POST.get('mn')
            i.address= request.POST.get('address')
            i.occupation=request.POST.get('occupation')
            i.loan=request.POST.get('loan')
            i.save()
            return render(request, 'insapp.html')
        else:
            return render(request, 'insapp wrong.html')

def ins2(request):
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('mn') and request.POST.get('address') and request.POST.get('occupation') and request.POST.get('loan'):
            i=insurance2()
            i.cid = request.session['cid']
            i.fname = request.POST.get('fname')
            i.lname = request.POST.get('lname')
            i.email = request.POST.get('email')
            i.mn = request.POST.get('mn')
            i.address= request.POST.get('address')
            i.occupation=request.POST.get('occupation')
            i.loan=request.POST.get('loan')
            i.save()
            return render(request, 'insapp.html')
        else:
            return render(request, 'insapp wrong.html')

