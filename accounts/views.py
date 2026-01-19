from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from .models import Account
from .forms import AccountForm, TransactionForm
import random
import string

class AccountListView(ListView):
    model = Account
    template_name = 'accounts/dashboard.html'
    context_object_name = 'accounts'

class AccountDetailView(DetailView):
    model = Account
    template_name = 'accounts/account_detail.html'
    context_object_name = 'account'

class AccountCreateView(CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounts/account_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        # Generate Account No
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=4)
        spchar = random.choices("!@#$%^&*()_+", k=1)
        full_id = alpha + num + spchar
        random.shuffle(full_id)
        account_no = "".join(full_id)
        
        form.instance.account_no = account_no
        messages.success(self.request, f"Account created! Number: {account_no}")
        return super().form_valid(form)

class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'accounts/account_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

def deposit_view(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            amount = form.cleaned_data['amount']
            
            if pin == account.pin:
                account.balance += amount
                account.save()
                messages.success(request, f"Deposited {amount} successfully.")
                return redirect('account_detail', pk=pk)
            else:
                messages.error(request, "Invalid PIN")
    else:
        form = TransactionForm()
    
    return render(request, 'accounts/transaction_form.html', {
        'form': form, 'account': account, 'action': 'Deposit'
    })

def withdraw_view(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            amount = form.cleaned_data['amount']
            
            if pin == account.pin:
                if account.balance >= amount:
                    account.balance -= amount
                    account.save()
                    messages.success(request, f"Withdrew {amount} successfully.")
                    return redirect('account_detail', pk=pk)
                else:
                    messages.error(request, "Insufficient Funds")
            else:
                messages.error(request, "Invalid PIN")
    else:
        form = TransactionForm()
    
    return render(request, 'accounts/transaction_form.html', {
        'form': form, 'account': account, 'action': 'Withdraw'
    })
