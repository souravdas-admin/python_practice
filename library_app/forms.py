from django import forms
from .models import BookIssue,Book,Member

class BookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['book','member']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'genre',
            'publication_year',
            'total_copies',
            'available_copies'
        ]

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = [
            'name',
            'email',
            'phone',
            'membership_date'
        ]