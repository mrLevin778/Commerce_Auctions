from django.shortcuts import render, get_object_or_404
from .models import Category, Auction


def auctions_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    auctions = Auction.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        auctions = auctions.filter(category=category)
    return render(request, 'auctions/auction/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'auctions': auctions
                  })


def auction_detail(request, id, slug):
    auction = get_object_or_404(Auction,
                                id=id,
                                slug=slug,
                                available=True
                                )
    return render(request, 'auctions/auction/detail.html',
                  {
                      'auction': auction
                  })
