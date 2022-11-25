from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from checkout.models import Order
from .models import UserAccount
from .forms import UserAccountForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserAccountForm(instance=profile)
    orders = profile.orders.all()

    template = 'users/profile.html'
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a previous orders with order number: ' +
        f'{order_number}. The confirmation sent to your' +
        f' email on {order.date:%d/%m/%Y %H:%M}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
