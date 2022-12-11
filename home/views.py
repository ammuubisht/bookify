from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import CommentForm, CreateUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def homepage(request):
    books = Book.objects.all().order_by("-id")
    book_titles = []
    for book in books:
        book_titles.append([book.book_name.lower(), book.slug])

    return render(request, 'home/homepage.html',{"books": books, 'book_titles': book_titles})

def book_detail(request, slug):
    identified_book = Book.objects.get(slug=slug)
    comment_form = CommentForm()

    books = Book.objects.all()
    book_titles = []
    for book in books:
        book_titles.append([book.book_name.lower(), book.slug])

    print(book_titles)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.book = identified_book
            comment_form.username = request.user.username
            comment_form.save()

            return HttpResponseRedirect(reverse('book-detail-page', args=[slug]))
        else:
            return render(request, 'home/book-detail.html', {"book": identified_book, "comment_form": comment_form})



    return render(request, 'home/book-detail.html', 
    {
    "book": identified_book, 
    "comment_form": comment_form, 
    'comments': identified_book.comments.all().order_by("-id"),
    'book_titles': book_titles
    })



def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    

    form = CreateUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username or password is incorrect')
            

    context = {'form': form}
    return render(request, 'home/login.html', context)



def signupPage(request):

    if request.user.is_authenticated:
        return redirect('/')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')

    context = {'form': form}
    return render(request, 'home/signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')

def profilePage(request):
    return render(request, 'home/profile.html')