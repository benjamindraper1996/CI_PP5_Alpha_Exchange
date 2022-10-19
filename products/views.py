"""
A module containing the views within products app.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from .models import Product, Category


def list_products(request, page=1):
    """
    Displays the list of products with filtering and search queries.
    """

    products = Product.objects.all()
    query = None
    categories = None

    # Search query filter
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Please enter some search criteria.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                    description__icontains=query) | Q(
                    recommended_use__icontains=query)
            products = products.filter(queries)

    paginator = Paginator(products, 20)  # Number to paginate by

    # Try to paginate
    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Displays the product details page by product ID.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product_detail.html', context)
