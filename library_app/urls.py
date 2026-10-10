from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_all_books,name='show_all_books'),
    path('add_book/',views.add_book,name='add_book'),
    path('update_book/<int:id>/',views.update_book,name='update_book'),
    path('delete_book/<int:id>/',views.delete_book,name='delete_book'),

    path('member_list/',views.show_all_members,name='show_all_members'),
    path('add_member/',views.add_member,name='add_member'),
    path('update_member/<int:id>/',views.update_member,name='update_member'),
    path('delete_member/<int:id>/',views.delete_member,name='delete_member'),

    path('issue_book/',views.issue_book,name='issue_book'),
    path('issued_book/',views.issued_book,name='issued_book'),
    path('return_book/<int:id>/', views.return_book, name='return_book'),

]