from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Delivery, username, DeliveryCharge
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .location import get_lat_long


@csrf_exempt
def add_item(request):
    if request.method == 'GET':
        data = 'Sample data from local server'  # Replace with actual logic
        return JsonResponse({'info': data})
    return JsonResponse({'error': 'Invalid request'}, status=400)


def home(request):
    return render(request, "home.html")


def user_view_delivery(request):
    names = username.objects.last()
    name = names.name
    delivery = Delivery.objects.filter(recipient_name=name)
    return render(request, "user_view_delivery.html", {'deliveries': delivery})


def login(request):
    return render(request, "login.html")


def logout(request):
    return render(request, "logout.html")


def dcharge(request):
    return render(request, "dcharge.html")


def user_admin_login(request):
    return render(request, "user_admin_login.html")


def user_home(request):
    return render(request, "user_home.html")


def admin_login(request):
    return render(request, "admin_login.html")


def user_sign_in(request):
    if request.method == "POST":
        name = request.POST.get('username')
        username.objects.create(name=name)
        return render(request, "user_home.html")
    return render(request, "user_sign_in.html")


def user_sign_up(request):
    return render(request, "user_sign_up.html")


@csrf_exempt
def add_delivery(request):
    if request.method == 'POST':
        recipient_name = request.POST.get('recipient_name')
        recipient_mobile_number = request.POST.get('recipient_mobile_number')
        pickup = request.POST.get('pickup')
        destination = request.POST.get('destination')
        product_type = request.POST.get('product_type')
        distance = request.POST.get('distance')
        weight = request.POST.get('weight')

        if not distance:
            return render(request, 'add_delivery.html')

        try:
            distance = float(distance)
        except ValueError:
            return render(request, 'add_delivery.html')

        if weight == '5005':
            weight_factor = 1.5
            weight = "500gm - 5kg"
        elif weight == '510':
            weight_factor = 2
            weight = "5kg - 10kg"
        elif weight == '1025':
            weight_factor = 3
            weight = "10kg - 25kg"
        else:
            return render(request, 'add_delivery.html')

        delivery_charge = distance * 0.5 * weight_factor
        delivery = Delivery.objects.create(
            recipient_name=recipient_name,
            recipient_mobile_number=recipient_mobile_number,
            pickup=pickup,
            destination=destination,
            product_type=product_type,
            distance=distance,
            weight=weight,
            delivery_charge=delivery_charge,
            status="Ordered"
        )

        request.session['delivery_id'] = delivery.id
        return redirect(f'/payment/?deliveryCharge={delivery_charge:.2f}')

    return render(request, 'add_delivery.html')


def payment(request):
    delivery_id = request.session.get('delivery_id', None)
    if delivery_id is None:
        return redirect(reverse('add_delivery'))

    delivery = Delivery.objects.get(id=delivery_id)

    if request.method == 'POST':
        request.session.pop('delivery_id', None)
        return redirect(reverse('admin_view_delivery'))

    return render(request,
                  'payment.html',
                  {'delivery': delivery,
                   'delivery_charge': delivery.delivery_charge})


def admin_home(request):
    return render(request, 'admin_home.html')


def admin_view_delivery(request):
    deliveries = Delivery.objects.all()
    return render(request,
                  'admin_view_delivery.html',
                  {'deliveries': deliveries})


@csrf_exempt
def calculate_delivery_charge(request):
    if request.method == 'POST':
        distance = request.POST.get('distance')
        weight = request.POST.get('weight')

        if not distance:
            return JsonResponse({'error': 'Distance is required'}, status=400)

        try:
            distance = float(distance)
        except ValueError:
            return JsonResponse({'error': 'Invalid distance'}, status=400)

        if weight == '5005':
            weight_factor = 1.5
        elif weight == '510':
            weight_factor = 2
        elif weight == '1025':
            weight_factor = 3
        else:
            return JsonResponse({'error': 'Invalid weight range'}, status=400)

        delivery_charge = distance * 5 * weight_factor

        return JsonResponse({'delivery_charge': delivery_charge})

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_coordinates(request):
    place_name = request.GET.get('place_name')
    coordinates = get_lat_long(place_name)
    if coordinates:
        return JsonResponse({'coordinates': coordinates})
    else:
        return JsonResponse({'coordinates': None})
