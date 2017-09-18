from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache

import MySQLdb as mdb

db=mdb.connect(host='localhost',port=3306,user='root',passwd='Chawla',db='DBMS')
cur=db.cursor()

cur_sem=1
cur_year=2016

@never_cache
def StudHome(request):
    if ('student' not in request.session):
        return redirect('/DBMSP1/home')
    var1=""
    if('student' in request.session):
        var1="Welcome "+request.session['student']

    return render(request,'student/StudentHome.html',{'var1':var1})

@never_cache
def profile(request):
    if ('student' not in request.session):
        return redirect('/DBMSP1/home')
    message=""
    try:
        roll1 = int(request.session['student'])
    except:
        return render(request, 'student/Error.html', {'message': 'Some unknown error occured'})

    try:
        cur.execute('select * from student where roll_no=%s', [roll1])
    except Exception as e:
        return render(request, 'student/Error.html', {'message': e})

    L = list(cur.fetchall()[0])

    name = L[1]
    mno = L[2]
    deptname = L[3]
    hostelid = int(L[4])
    roomno = int(L[5])
    dob = L[6]

    gender = L[7]
    email = L[8]
    return render(request,'student/Profile.html',{'name':name,'mno':mno,'deptname':deptname,'hostelid':hostelid
                                                  ,'dob':dob,'roomno':roomno,'gender':gender,'email':email,'username':roll1,'message':message})


@never_cache
def ProfileUpdate(request):
    if ('student' not in request.session):
        return redirect('/DBMSP1/home')
    message=""
    try:
        roll1 = int(request.session['student'])
    except:
        return render(request, 'student/Error.html', {'message': 'Some unknown error occured'})

    try:
        cur.execute('select * from student where roll_no=%s', [roll1])
    except Exception as e:
        return render(request, 'student/Error.html', {'message': e})

    L = list(cur.fetchall()[0])
    name = L[1]
    mno = L[2]
    deptname = L[3]
    hostelid = int(L[4])
    roomno = int(L[5])
    dob = L[6]

    gender = L[7]
    email = L[8]


    try:
        roll=request.POST['username']
        HostelId1=request.POST['hostelid']
        Roomno1=request.POST['roomno']
        name1 = request.POST['name']
        dob1 = request.POST['dob']
        gender1=request.POST['gender']
        email_id1=request.POST['email']
        num1=request.POST['mno']
        deptname1=request.POST['deptname']
    except:
        message="Some Unknown error"
        return render(request, 'student/Error.html', {'message': message})

    try:
        cur.execute('update student set stud_name=%s,contact_no=%s,dept_name=%s,hostel_id=%s,room_no=%s,dateofbirth=%s,gender=%s, email=%s where roll_no=%s',
                    [name1,num1,deptname1,int(HostelId1),int(Roomno1),dob1,gender1,email_id1,int(roll)])
    except Exception as e:
        message=e
        return render(request, 'student/Error.html', {'message': e})

    db.commit()

    return render(request, 'student/Success.html')


@never_cache
def info(request):
    if ('student' not in request.session):
        return redirect('/DBMSP1/home')
    return render(request,'student/info.html')


@never_cache
def EnrolledCourses(request):
    if ('student' not in request.session):
        return redirect('/DBMSP1/home')

    roll=int(request.session['student'])

    try:
        cur.execute('select course_id,attendance from stud_sec where roll_no=%s',[roll])
    except Exception as e:
        return render(request,'student/info.html',{'var1':e})

    L=cur.fetchall()
    print(L)
    return render(request,'student/enrolled.html',{'L':L})






@never_cache
def signout(request):
    if ('student' not in request.session):
        return redirect('/DBMSP1/home')
    if ('admin' in request.session):
        del request.session['admin']

    if ('student' in request.session):
        del request.session['student']

    if ('faculty' in request.session):
        del request.session['faculty']

    return redirect('../../../home')


@never_cache
def completed(request):

    if ('student' not in request.session):
        return redirect('/DBMSP1/home')

    roll = int(request.session['student'])

    try:
        cur.execute('select course_id,grade from stud_sec where roll_no=%s and (year<%s or (semester<%s and year=%s))', [roll,cur_year,cur_sem,cur_year])
    except Exception as e:
        return render(request, 'student/Error.html' ,{'message':e})


    L = cur.fetchall()
    return render(request, 'student/completed.html',{'L':L})


