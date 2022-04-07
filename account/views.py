from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from .forms import AccountForm

# def account_view(request):
#     account = Account.objects.filter(user=request.user)
#     return render(request, 'account/account.html', {'account':account})


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


def account(request):
    account = Account.objects.filter(user=request.user)
    return render(request, 'account/account.html', {'account': account})



def account_update(request): # working 
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


def account_delete(request):
    acc = get_object_or_404(Account, user = request.user)
    if request.method == 'GET':
        return render(request, 'account/account_delete.html', {'acc': acc})
    else:
        acc.delete()
        return redirect('account')


# def tag_delete(request, slug):
#     tag = get_object_or_404(Tag, slug__iexact=slug, user= request.user)
#     if request.method == 'GET':
#         return render(request, 'todo/tag_delete.html', {'tag':tag})
#     else:
#         tag.delete()
#         return redirect('tags')

# @login_required
# def tag_update(request, slug):
#     tag = get_object_or_404(Tag, slug__iexact=slug, user= request.user)
#     if request.method == 'GET':
#         form = TagForm(instance=tag)
#         return render(request, 'todo/tag_update.html', {'tag':tag, 'form':form})
#     else:
#         try:
#             form = TagForm(request.POST, instance=tag)
#             form.save()
#             return redirect('tags')
#         except ValueError:
#             return render(request, 'todo/tag_update.html', {'tag': tag, 'form': form})

# def tags(request):
#     tags = Tag.objects.filter(user=request.user)
#     return render(request, 'todo/tags.html', {'tags':tags})


# @login_required
# def viewtodo(request, todo_pk):
#     error = 'Bad info'
#     todo = get_object_or_404(Todo, pk=todo_pk, user= request.user)
#     if request.method == 'GET':
#         form = TodoForm(instance=todo)
#         return render(request, 'todo/viewtodo.html', {'todo': todo,
#                                                       'form': form})
#     else:
#         try:
#             form = TodoForm(request.POST, instance=todo)
#             form.save()
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, 'todo/viewtodo.html', {'todo': todo,
#                                                           'form': form,
#                                                           'error': error})

# @login_required
# def createtodo(request):
#     error = 'Bad data passed in. Plese try again.'
#     if request.method == 'GET':
#         return render(request, 'todo/createtodo.html', {'form': TodoForm()})
#     else:
#         try:
#             form = TodoForm(request.POST)
#             newtodo = form.save(commit=False)
#             newtodo.user = request.user
#             newtodo.save()
#             for tag in form.cleaned_data['tags']:
#                 newtodo.tags.add(tag)
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, 'todo/createtodo.html', {'form': TodoForm(),
#                                                             'error': error})