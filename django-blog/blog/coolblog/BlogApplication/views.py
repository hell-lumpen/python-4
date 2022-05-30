from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .forms import ReviewForm
from .models import *
from django.shortcuts import get_object_or_404


def main_page(request):
    reviews = Review.objects.order_by("pk")[::-1]
    reviews = reviews[:3:]
    digests = Digest.objects.order_by("pk")[::-1]
    digests = digests[:3:]
    # срез [:-4:-1] почему-то вызывает ошибку
    return render(request, 'BlogApplication/main_page.html', {"reviews": reviews, "digests": digests})


def create_new_review(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'

    form = ReviewForm()

    return render(request, 'BlogApplication/create_form.html', {
        'form': form,
        'error': error
    })


def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        review.title = request.POST.get('title')
        review.review_text = request.POST.get('review_text')
        review.save()
        return redirect('home')
    else:
        return render(request, 'BlogApplication/edit_form.html', {
            'review': review
        })


def about(request):
    return render(request, 'BlogApplication/about.html')


def author(request):
    return render(request, 'BlogApplication/author.html')


def get_all_reviews(request):
    reviews = Review.objects.order_by("pk")[::-1]
    return render(request, 'BlogApplication/all_reviews.html', {"reviews": reviews})


def get_all_digests(request):
    digests = Digest.objects.order_by("pk")[::-1]
    return render(request, 'BlogApplication/all_digests.html', {"digests": digests})


def get_review_by_id(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'BlogApplication/review.html', {"review": review})


def get_digest_by_id(request, digest_id):
    digest = get_object_or_404(Digest, pk=digest_id)
    return render(request, 'BlogApplication/digest.html', {"digest": digest})


def page_not_found(request, exception):
    return render(request, 'BlogApplication/404notfound.html')
