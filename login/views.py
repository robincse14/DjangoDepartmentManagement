from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache


import MySQLdb as mdb

db=mdb.connect(host='localhost',port=3306,user='root',passwd='Chawla',db='DBMS')
cur=db.cursor()

#Student SignUp

@never_cache
def signup(request):
    if ('admin' in request.session):
        return redirect('../../../authuser/AuthUserHome/')

    if ('faculty' in request.session):
        return redirect('../../../faculty/FacultyHome/')

    if ('student' in request.session):
        return redirect('../../../student/StudHome/')
    return render(request,'login/signup.html')

@never_cache
def login(request):
    print("here")

    if ('admin' in request.session):
        return redirect('../../../authuser/AuthUserHome/')

    if ('faculty' in request.session):
        return redirect('../../../faculty/FacultyHome/')

    if ('student' in request.session):
        return redirect('../../../student/StudHome/')

    return render(request,'login/login.html')

@never_cache
def facultysignup(request):
    return render(request,'login/facultysignup.html')

@never_cache
def AfterFacultySignup(request):

    try:
        id = request.POST['Username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        passwd = request.POST['pwd']
        cpasswd = request.POST['cpwd']
        deptname = request.POST['deptname']
    except:
        return render(request, 'login/Error.html', {'message': 'Some unknown error occured '})

    try:
        k=int(id)
    except:
        return render(request, 'login/Error.html', {'message': 'Id must be type int '})
    salary=100000
    if (passwd != cpasswd):
        return render(request, 'login/Error.html', {'message': 'Password and Confirm Password does not match'})

    try:
        cur.execute('select count(*) from instructor where id=%s',[int(id)])
    except:
        return render(request, 'login/Error.html', {'message': 'Some unknown error occured'})
    db.rollback()

    tt=cur.fetchall()
    if(int(tt[0][0])!=0):
        return render(request, 'login/Error.html', {'message': 'username already in use'})

    try:
        cur.execute('insert into instructor values(%s,%s,%s,%s,%s)',[int(id),fname + " " +lname,int(salary),deptname,passwd])
    except:
        return render(request, 'login/Error.html', {'message': 'error occured. Make sure values entered are of correct type'})

    db.commit()

    return render(request, 'login/Success.html')







@never_cache
def AfterSignup(request):


    if ('admin' in request.session):
        return redirect('../../../../authuser/AuthUserHome/')

    if ('faculty' in request.session):
        return redirect('../../../../faculty/FacultyHome/')

    if ('student' in request.session):
        return redirect('../../../../student/StudHome/')

    try:
        roll=request.POST['Username']
        HostelId=request.POST['HostelId']
        Roomno=request.POST['roomno']
        fname=request.POST['firstname']
        lname = request.POST['lastname']
        dob = request.POST['dob']
        gender=request.POST['gender']
        email_id=request.POST['eml']
        passwd=request.POST['pwd']
        cpasswd=request.POST['cpwd']
        num=request.POST['mno']
        deptname=request.POST['deptname']

    except:
        return render(request, 'login/Error.html', {'message': 'Some unknown error occured '})

    #Checking errors

    if(passwd!=cpasswd):
        return render(request, 'login/Error.html', {'message': 'Password and Confirm Password does not match'})

    if(len(passwd)<8 or len(passwd)>15):
        return render(request,'login/Error.html',{'message': 'Password lenght must be between 8 and 15 characters'})

    try:
        k=int(roll)
    except:
        return render(request, 'login/Error.html', {'message': 'Username must be integer'})

    cur.execute('select count(*) from student where email=%s or Roll_no=%s',[email_id,int(roll)])

    if int(cur.fetchall()[0][0]) != 0:
        return render(request, 'login/Error.html', {'message': 'email or username already in use'})

    db.rollback()

    print(int(roll),fname+ " " + lname,num,deptname,int(HostelId),int(Roomno),dob,gender,email_id,passwd)

    try:
        cur.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[int(roll),fname+ " " + lname,num,deptname,int(HostelId),int(Roomno),dob,gender,email_id,passwd])
    except Exception as e:
        return render(request, 'login/error.html', {'message':e})

    db.commit()

    return render(request, 'login/Success.html')


@never_cache
def Afterlogin(request):
    print("here")

    if ('admin' in request.session):
        return redirect('../../../../authuser/AuthUserHome/')

    if ('faculty' in request.session):
        return redirect('../../../../faculty/FacultyHome/')

    if ('student' in request.session):
        return redirect('../../../../student/StudHome/')


    try:
        username=str(request.POST['Username'])
        pwd=str(request.POST['pwd'])
        person=str(request.POST['person'])
    except:
        return render(request, 'login/Error.html', {'message': 'Some unknown error occured'})


    try:
        k=int(username)
    except:
        return render(request, 'login/Error.html', {'message': 'Username does not exist'})

    username_int = int(username)
    print(person)

    if(person =="admin"):
        cur.execute('select pass from admin where username=%s',[username_int])
        tt=cur.fetchall()
       # print(tt)
        if (len(tt)== 0):
            return render(request, 'login/Error.html', {'message': 'Username does not exist'})
        value=tt[0][0]
        if(value!=pwd):
            return render(request, 'login/Error.html', {'message': 'Password does not match'})
        request.session['admin']=username
        return redirect('../../../../authuser/AuthUserHome/')

    elif (person=="student"):
        cur.execute('select pass from student where Roll_no=%s;',[username_int])
        tt = cur.fetchall()

        if(len(tt)==0):
            return render(request, 'login/Error.html', {'message': 'Username does not exist'})

        value = tt[0][0]
        if (value != pwd):
            return render(request, 'login/Error.html', {'message': 'Password does not match'})
        request.session['student']=username
        return redirect('../../../../student/StudHome/')

    else:
        cur.execute('select password from instructor where id=%s',[username_int])
        tt = cur.fetchall()
        if (len(tt) == 0):
            return render(request, 'login/Error.html', {'message': 'Username does not exist'})
        value = tt[0][0]
        if (value != pwd):
            return render(request, 'login/Error.html', {'message': 'Password does not match'})
        request.session['faculty']=username
        return redirect('../../../../faculty/FacultyHome/')




@never_cache
def home(request):
    var1=""
    if ('admin' in request.session):
        var1= "Welcome "+request.session['admin']

    if ('student' in request.session):
        var1="Welcome "+request.session['student']

    if ('faculty' in request.session):
        var1="Welcome "+request.session['faculty']
    return render(request,'login/home.html',{'var1':var1})



@never_cache
def signout(request):
    if ('admin' in request.session):
        del request.session['admin']

    if ('student' in request.session):
        del request.session['student']

    if ('faculty' in request.session):
        del request.session['faculty']

    return redirect('/DBMSP1/home/')



