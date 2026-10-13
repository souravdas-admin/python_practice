from django.db import transaction
from django.db.models import F
from datetime import date, timedelta
from django.shortcuts import render,redirect
from .models import Book,BookIssue,Member
from .forms import BookIssueForm,BookForm,MemberForm

# Create your views here.
def show_all_books(request):
    all_books = Book.objects.all()
    return render(request,'library/book_list.html',{'all_books':all_books})

def add_book(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect('show_all_books')
    else:
        book_form = BookForm()
    return render(request,'library/add_book.html',{'book_form':book_form})

def update_book(request,id):
    specific_book = Book.objects.get(id=id)
    if request.method == "POST":
        book_form = BookForm(request.POST,instance=specific_book)
        if book_form.is_valid():
            book_form.save()
            return redirect('show_all_books')
    else:
        book_form = BookForm(instance=specific_book)
    return render(request,'library/update_book.html',{'book_form':book_form})

def delete_book(request,id):
    specific_book = Book.objects.get(id=id)
    if request.method == 'POST':
        specific_book.delete()
        return redirect('show_all_books')
    else:
        return render(request,'library/delete_book.html',{'specific_book':specific_book})



def show_all_members(request):
    all_members = Member.objects.all()
    return render(request,'library/member_list.html',{'all_members':all_members})

def add_member(request):
    if request.method == 'POST':
        member_form = MemberForm(request.POST)
        if member_form.is_valid():
            member_form.save()
            return redirect('show_all_members')
    else:
        member_form = MemberForm()
    return render(request,'library/add_member.html',{'member_form':member_form})

def update_member(request,id):
    specific_member = Member.objects.get(id=id)
    if request.method == "POST":
        member_form = MemberForm(request.POST,instance=specific_member)
        if member_form.is_valid():
            member_form.save()
            return redirect('show_all_members')
    else:
        member_form = MemberForm(instance=specific_member)
    return render(request,'library/update_member.html',{'member_form':member_form})

def delete_member(request,id):
    specific_member = Member.objects.get(id=id)
    if request.method == 'POST':
        specific_member.delete()
        return redirect('show_all_members')
    else:
        return render(request,'library/delete_member.html',{'specific_member':specific_member})


def issued_book(request):
    books_issued = BookIssue.objects.all()
    return render(request,'library/issued_book.html',{'books_issued':books_issued})


def issue_book(request):
    if request.method == "POST":
        book_form = BookIssueForm(request.POST)
        if book_form.is_valid():
            issue = book_form.save(commit=False)
            with transaction.atomic():
                updated = Book.objects.filter(id=issue.book_id,available_copies__gt=0).update(available_copies=F('available_copies')-1)
                if updated:
                    issue.due_date = date.today()+timedelta(days=7)
                    issue.save()
                    return redirect('issued_book')
                book_form.add_error('book', 'This book is not available.') 
    else:
        book_form = BookIssueForm()
    return render(request,'library/issue_book.html',{'book_form':book_form})

def return_book(request,id):
    issue = BookIssue.objects.get(id=id)
    if request.method == 'POST':
        with transaction.atomic():
            issue.return_date = date.today()
            issue.book.available_copies += 1
            issue.book.save()
            issue.save()
            return redirect('issued_book')
    else:
        return render(
            request,
            'library/return_book.html',
            {'issue': issue}
        )
print("views.py executed successfully")