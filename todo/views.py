from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TagForm, TodoForm
from .models import Todo, Tag
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'todo/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                error = 'That username has already been taken. Please choose a new username'
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),
                                                                'error': error})
        else:
            error = 'Password did not match'
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(),
                                                            'error': error})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if user is None:
            error = 'Username and password did not match'
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(),
                                                           'error': error})
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def createtodo(request):
    error = 'Bad data passed in. Plese try again.'
    if request.method == 'GET':
        return render(request, 'todo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            for tag in form.cleaned_data['tags']:
                newtodo.tags.add(tag)
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {'form': TodoForm(),
                                                            'error': error})


@login_required
def currenttodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todo/currenttodos.html', {'todos': todos})


@login_required
def completedtodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todo/completedtodos.html', {'todos': todos})


@login_required
def viewtodo(request, todo_pk):
    error = 'Bad info'
    todo = get_object_or_404(Todo, pk=todo_pk, user= request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo,
                                                      'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo,
                                                          'form': form,
                                                          'error': error})


@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')


@login_required
def tags(request):
    tags = Tag.objects.all()
    return render(request, 'todo/tags.html', {'tags':tags})

@login_required
def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'todo/tag_detail.html', {'tag':tag})


def tag_create(request):
    if request.method == 'GET':
        return render(request, 'todo/tag_create.html', {'form': TagForm()})
    else:
        try:
            form = TagForm(request.POST)
            new_tag = form.save(commit=False)
            new_tag.user = request.user
            new_tag.save()
            return redirect(new_tag)
        except ValueError:
            return render(request, 'todo/tag_create.html', {'form': form})


#UPDATING THE TAG
def tag_update(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    if request.method == 'GET':
        form = TagForm(instance=tag)
        return render(request, 'todo/tag_update.html', {'tag':tag, 'form':form})
    else:
        try:
            form = TagForm(request.POST, instance=tag)
            form.save()
            return redirect('tags')
        except ValueError:
            return render(request, 'todo/tag_update.html', {'tag': tag, 'form': form})


def tag_delete(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    if request.method == 'GET':
        return render(request, 'todo/tag_delete.html', {'tag':tag})
    else:
        tag.delete()
        return redirect('tags')


# @login_required
# def tag_create(request):
#     if request.method == 'GET':
#         return render(request, 'todo/tag_create.html', {'form': TagForm()})
#     else:
#         form = TagForm(request.POST)
#         if form.is_valid():
#             new_tag = form.save(commit=False)
#             new_tag.user = request.user
#             new_tag.save()
#             return redirect(new_tag)
#         return render(request, 'todo/tag_create.html', {'form': form})