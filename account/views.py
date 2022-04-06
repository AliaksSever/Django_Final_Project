from django.shortcuts import render, redirect
from .models import Account
from .forms import AccountForm

# def account_view(request):
#     account = Account.objects.filter(user=request.user)
#     return render(request, 'account/account.html', {'account':account})


def account_view(request):
    error = 'Bad data passed in. Plese try again.'
    if request.method == 'GET':
        return render(request, 'account/account.html', {'form':AccountForm()})
    else:
        try:
            form = AccountForm(request.POST)
            info = form.save(commit=False)
            info.user = request.user
            info.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'account/account.html', {'form':AccountForm(), 'error':error})


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