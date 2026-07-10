from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from .models import *
from .forms import *




@login_required
def DashBoardPage(request):
    cash = AddCashModel.objects.filter(user=request.user).aggregate(total = Sum('amount'))['total'] or 0
    expense = ExpenseModel.objects.filter(user=request.user).aggregate(total = Sum('amount'))['total'] or 0
    remain = cash - expense
    Cdata = AddCashModel.objects.filter(user=request.user)
    Edata = ExpenseModel.objects.filter(user=request.user)
    if cash >= 500000:
        tax= cash-500000        
        ptax = tax*(0.1)
    else:
        tax = 0
        ptax = 0
    


    cont={
        'cash':cash,
        'expense':expense,
        'remain':remain,
        'Cdata':Cdata,
        'Edata':Edata,
        'tax':tax,
        'ptax':ptax,
    }
    return render(request, 'pages/dashboard.html', cont)




def RegsiterPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Creation Successful')
            return redirect('login')
    else:
        form = RegisterForm()

    cont ={
        'form':form,
        'title':'Register Form',
        'btn': 'Register'
    }
    return render(request, 'base/baseForm.html', cont)



def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('dashboard')
    else:
        form = LoginForm()

    cont ={
        'form':form,
        'title':'Login Form',
        'btn': 'Login',
    }
    return render(request, 'base/baseForm.html', cont)

@login_required
def LogoutPage(request):
    logout(request)
    messages.warning(request, 'You are logged out')
    return redirect('dashboard')



@login_required
def AddcashPage(request, id=None):
    if id:
        data=AddCashModel.objects.get(id=id)
        title='Update Cash Details'
        btn = 'Update'
    else:
        data=None
        title='Add Cash Details'
        btn = 'Add'
    if request.method == 'POST':
        form = AddCashForm(request.POST, instance=data)
        if form.is_valid():
            cash = form.save(commit=False)
            cash.user = request.user
            cash.save()
            if id:
                messages.success(request, 'Cash Updated Successfully')
            else:
                messages.success(request, 'Cash Added Successfully')

            return redirect('dashboard')
    else:
        form = AddCashForm(instance=data)

    cont ={
        'form':form,
        'title':title,
        'btn': btn
    }
    return render(request, 'base/baseForm.html', cont)

@login_required
def DeleteCashPage(request,id):
    AddCashModel.objects.get(id=id).delete()
    messages.error(request, 'Cash Deleted')
    return redirect('dashboard')


@login_required
def ExpensePage(request, id=None):
    if id:
        data = get_object_or_404(ExpenseModel, id=id)
        title = 'Update Expense Details'
        btn='Update'
    else:
        data=  None
        title= 'Add Expense Details'
        btn = 'Add'
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance = data)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()

            if id:
                messages.success(request, 'Expense Updated Successfully')
            else:
                messages.success(request, 'Expense Added Successfully')
            return redirect('dashboard')
    else:
        form = ExpenseForm(instance = data)
    
    cont ={
        'form':form,
        'title': title,
        'btn': btn
    }
    return render(request, 'base/baseForm.html', cont)

@login_required
def DeleteExpensePage(request,id):
    ExpenseModel.objects.get(id=id).delete()
    messages.error(request, 'Expense Deleted')
    return redirect('dashboard')




# Create your views here.
