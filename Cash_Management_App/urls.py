from django.urls import path
from .views import *

urlpatterns = [
    path('', DashBoardPage, name='dashboard'),

    path('register/', RegsiterPage, name='register'),
    path('login/', LoginPage, name='login'),
    path('logout/', LogoutPage, name='logout'),

    path('addCash/', AddcashPage, name='addCash'),
    path('editCash/<str:id>/', AddcashPage, name='editCash'),
    path('delCash/<str:id>/', DeleteCashPage, name='delCash'),

    path('addExpense/', ExpensePage, name='addExpense'),
    path('editExpense/<str:id>/', ExpensePage, name='editExpense'),
    path('delExpense/<str:id>/', DeleteExpensePage, name='delExpense'),
]