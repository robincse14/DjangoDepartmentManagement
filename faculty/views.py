from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache

import MySQLdb as mdb

db=mdb.connect(host='localhost',port=3306,user='root',passwd='Chawla',db='DBMS')
cur=db.cursor()

@never_cache
def FacultyHome(request):
    if ('faculty' not in request.session):
        return redirect('/DBMSP1/home')

    if('faculty' in request.session):
        var1="Welcome " + request.session['faculty']

    return render(request,'faculty/faculltyhome.html',{'var1':var1})

@never_cache
def profile(request):
    if ('faculty' not in request.session):
        return redirect('/DBMSP1/home')

    message = ""
    try:
        id = int(request.session['faculty'])
    except:
        return render(request, 'faculty/Error.html', {'message': 'Some unknown error occured'})

    try:
        cur.execute('select * from instructor where id=%s', [id])
    except Exception as e:
        return render(request, 'faculty/Error.html', {'message': 'Some unknown error occured'})

    L = list(cur.fetchall()[0])

    name = L[1]
    deptname = L[3]

    return render(request, 'faculty/profile.html', {'name': name,  'deptname': deptname,
          'username': id ,'message': message})






@never_cache
def signout(request):
    if ('faculty' not in request.session):
        return redirect('/DBMSP1/home')
    if ('admin' in request.session):
        del request.session['admin']

    if ('student' in request.session):
        del request.session['student']

    if ('faculty' in request.session):
        del request.session['faculty']

    return redirect('../../../home')

@never_cache
def update(request):
    if ('faculty' not in request.session):
        return redirect('/DBMSP1/home')
    message = ""
    try:
        id = int(request.session['faculty'])
    except:
        return render(request, 'faculty/Error.html', {'message': 'Some unknown error occured'})

    try:
        cur.execute('select * from instructor where id=%s', [id])
    except Exception as e:
        return render(request, 'faculty/Error.html', {'message': e})

    L = list(cur.fetchall()[0])

    name = L[1]
    deptname = L[3]

    try:
        fname=request.POST['name']
        fid=int(request.POST['username'])
        fdeptname=request.POST['deptname']
    except Exception as e:
        return render(request, 'faculty/Error.html', {'message': e})

    try:
        cur.execute('update instructor set teacher_name=%s,dept_name=%s where id=%s',[fname,fdeptname,id])
    except Exception as e:
        return render(request, 'faculty/Error.html', {'message': e})

    db.commit()

    return render(request, 'faculty/Success.html')

@never_cache
def selectedstud(request):
    if ('faculty' not in request.session):
        return redirect('/DBMSP1/home')
    return render(request,'faculty/selectstud.html')

@never_cache
def selectedstudvali(request):
    if ('faculty' not in request.session):
        return redirect('/DBMSP1/home')
    try:
        sem=request.POST['sem']
        year=request.POST['year']
        cid=request.POST['cid']
        sid=request.POST['sid']
    except:
        return render(request,'faculty/Error.html',{'message':'Some unknown error'})

    try:
        sem=int(sem)
        year=int(year)
        cid=int(cid)
        sid=int(sid)
    except:
        return render(request, 'faculty/Error.html', {'message': 'Entered values must be of int type'})


    try:
        cur.execute('select count(*) from stud_sec where semester=%s and year=%s and course_id=%s and roll_no=%s',[sem,year,cid,sid])
    except Exception as e:
        return render(request, 'faculty/Error.html', {'message': e})

    L=cur.fetchall()

    if(L[0][0]==0):
        return render(request, 'faculty/Error.html', {'message': 'Values does not match with any student'})

    cur.execute('select grade from stud_sec where semester=%s and year=%s and course_id=%s and roll_no=%s and grade is NOT NULL',[sem, year, cid, sid])


    L=cur.fetchall()
    grade=L[0][0]

    return render(request,'faculty/marks.html',{'grade':grade,'sem':sem,'year':year,'cid':cid,'sid':sid})

@never_cache
def change(request):
    if ('faculty' not in request.session):
        return redirect('/DBMSP1/home')
    try:
        grd=request.POST['grd']
        sem = int(request.POST['sem'])
        year = int(request.POST['year'])
        cid = int(request.POST['cid'])
        sid = int(request.POST['sid'])

    except:
        return render(request, 'faculty/Error.html', {'message':'Some unknown error'})
    try:
        grd=int(grd)
    except:
        return render(request, 'faculty/Error.html', {'message': 'Grade should be integer'})

    if(grd<0 or grd>10):
        return render(request, 'faculty/Error.html', {'message': 'Grade should be between 1 to 10'})

    print(grd)

    try:
        cur.execute('update stud_sec set grade=%s where semester=%s and year=%s and course_id=%s and roll_no=%s',[grd,sem,year,cid,sid])
    except Exception as e:
        return render(request, 'faculty/Error.html', {'message': e})

    db.commit()


    return render(request, 'faculty/Success.html', {'message': 'Updated'})




