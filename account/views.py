from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from .forms import AccountForm
from django.contrib.auth.decorators import login_required



@login_required
def account_view(request):
    error = 'Bad data passed in. Plese try again.'
    if request.method == 'GET':
        return render(request, 'account/account_view.html', {'form':AccountForm()})
    else:
        try:
            form = AccountForm(request.POST)
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('account')
        except ValueError:
            return render(request, 'account/account_view.html', {'form':AccountForm(), 'error':error})


@login_required
def account(request):
    account = Account.objects.filter(user=request.user)
    return render(request, 'account/account.html', {'account': account})


@login_required
def account_update(request):
    acc = get_object_or_404(Account, user = request.user)
    error = 'Bad info'
    if request.method == 'GET':
        form = AccountForm(instance=acc)
        return render(request, 'account/account_update.html', {'acc':acc, 'form': form})
    else:
        try:
            form = AccountForm(request.POST, instance=acc)
            form.save()
            return redirect('account')
        except ValueError:
            return render(request, 'account/account_update.html', {'acc':acc, 'form': form, 'error': error})


@login_required
def account_delete(request):
    acc = get_object_or_404(Account, user = request.user)
    if request.method == 'GET':
        return render(request, 'account/account_delete.html', {'acc': acc})
    else:
        acc.delete()
        return redirect('account')