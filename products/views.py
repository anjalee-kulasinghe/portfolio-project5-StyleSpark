from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category

def all_products(request):
    """ A view to show all products, including sorting and search queries """
    products = Product.objects.all()
    query = None
    categories = None
    sort = request.GET.get('sort', None)
    direction = request.GET.get('direction', 'asc')

    # Fetch all categories for the dropdown menu
    all_categories = Category.objects.all()

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET.getlist('category')
            if categories:
                products = products.filter(category__name__in=categories)
                categories = Category.objects.filter(name__in=categories)
            else:
                categories = None

        if 'q' in request.GET:
            query = request.GET['q']
            if query:
                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)
            else:
                messages.error(request, "You didn't enter any search criteria!")

    current_sorting = f'{sort}_{direction}' if sort and direction else None

    # Extracting names from all_categories queryset
    all_category_names = list(all_categories.values_list('name', flat=True))

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'all_categories': all_category_names,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)
