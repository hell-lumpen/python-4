from django.contrib import admin
from django.urls import path

from BlogApplication.views import *

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', main_page, name='home'),
    path('about/', about, name='about'),
    path('author/', author, name='author'),
    path('new_post/', create_new_review, name='new_post'),
    path('edit_post/<int:review_id>/', edit_review, name='edit_post'),
    path('digests/', get_all_digests, name='digests'),
    path('reviews/', get_all_reviews, name='reviews'),
    path('digests/<int:digest_id>/', get_digest_by_id, name='digest_by_id'),
    path('reviews/<int:review_id>/', get_review_by_id, name='reviews_by_id'),
]

handler404 = page_not_found
