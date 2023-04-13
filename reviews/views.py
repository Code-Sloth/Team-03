from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.

def index(request):
    reviews = Review.objects.all().order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'reviews/create.html', context)
        

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    context = {
        'review': review
    }
    return render(request, 'reviews/detail.html', context)