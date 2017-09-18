from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponseRedirect
from django.views.decorators.cache import never_cache

import MySQLdb as mdb

db=mdb.connect(host='localhost',port=3306,user='root',passwd='Chawla',db='DBMS')
cur=db.cursor()

@never_cache
def AuthUserHome(request):
    if('admin' not in request.session):
        return redirect('/DBMSP1/home')

    return render(request,'authuser/AdminHome.html')


@never_cache
def signout(request):
    if ('admin' not in request.session):
        return redirect('/DBMSP1/home')

    if ('admin' in request.session):
        del request.session['admin']

    if ('student' in request.session):
        del request.session['student']

    if ('faculty' in request.session):
        del request.session['faculty']

    return redirect('../../../home')

@never_cache
def addfaculty(request):
    if ('admin' not in request.session):
        return redirect('/DBMSP1/home')
    return redirect('../../login/faculty/signup/')

@never_cache
def deletefaculty(request):
    if ('admin' not in request.session):
        return redirect('/DBMSP1/home')
    return render(request, 'authuser/deletefaculty.html')

@never_cache
def deletefacultyvali(request):
    if ('admin' not in request.session):
        return redirect('/DBMSP1/home')
    try:
        id=request.POST['id']
    except:
        return render(request,'authuser/Error.html' , {'message':'Some unknown error'})

    try:
        id=int(id)
    except:
        return render(request, 'authuser/Error.html', {'message': 'Id must be of integer type'})

    try:
        cur.execute('select count(*) from instructor where id=%s',[id])
    except Exception as e:
        return render(request, 'authuser/Error.html', {'message': e})

    L = cur.fetchall()
    if(L[0][0]==0):
        return render(request, 'authuser/Error.html', {'message': 'Faculty with Specified id does not exist'})

    try:
        cur.execute('delete from instructor where id=%s',[id])
    except Exception as e:
        return render(request, 'authuser/Error.html', {'message': e})
    db.commit()

    return render(request, 'authuser/Success.html')

@never_cache
def deletestudent(request):
    if ('admin' not in request.session):
        return redirect('/DBMSP1/home')
    return render(request, 'authuser/deletestudent.html')

@never_cache
def deletestudentvali(request):
    if ('admin' not in request.session):
        return redirect('/DBMSP1/home')
    try:
        id = request.POST['id']
    except:
        return render(request, 'authuser/Error.html', {'message': 'Some unknown error'})

    try:
        id = int(id)
    except:
        return render(request, 'authuser/Error.html', {'message': 'Id must be of integer type'})

    try:
        cur.execute('select count(*) from student where roll_no=%s', [id])
    except Exception as e:
        return render(request, 'authuser/Error.html', {'message': e})

    L = cur.fetchall()
    if (L[0][0] == 0):
        return render(request, 'authuser/Error.html', {'message': 'Student with Specified id does not exist'})

    try:
        cur.execute('delete from student where roll_no=%s', [id])
    except Exception as e:
        return render(request, 'authuser/Error.html', {'message': e})

    db.commit()

    return render(request, 'authuser/Success.html')

@never_cache
def viewinfo(request):
    return render(request, 'authuser/viewinfo.html')

@never_cache
def viewstudent(request):
    return render(request,'authuser/viewstudent.html')

@never_cache
def viewstudentvali(request):
    try:
        id = request.POST['id']
    except:
        return render(request, 'authuser/Error.html', {'message': 'Some unknown error'})

    try:
        id=int(id)
    except:
        return render(request, 'authuser/Error.html', {'message': 'Id must be of int type'})

    try:
        cur.execute('select * from student where roll_no=%s',[id])
    except Exception as e:
        return render(request, 'authuser/Error.html', {'message': e})

    L=cur.fetchall()

    if(len(L)==0):
        return render(request, 'authuser/Error.html', {'message': 'User does not exist'})

    return render(request, 'authuser/viewstudentvali.html', {'L':L})




@never_cache
def viewfaculty(request):
    return render(request,'authuser/viewfaculty.html')

@never_cache
def viewfacultyvali(request):
    try:
        id = request.POST['id']
    except:
        return render(request, 'authuser/Error.html', {'message': 'Some unknown error'})

    try:
        id=int(id)
    except:
        return render(request, 'authuser/Error.html', {'message': 'Id must be of int type'})

    try:
        cur.execute('select * from instructor where id=%s',[id])
    except Exception as e:
        return render(request, 'authuser/Error.html', {'message': e})

    L=cur.fetchall()

    if(len(L)==0):
        return render(request, 'authuser/Error.html', {'message': 'User does not exist'})

    return render(request, 'authuser/viewfacultyvali.html', {'L':L})