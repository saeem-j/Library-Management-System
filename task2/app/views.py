from django.shortcuts import render

def menu(request):
    item=[
        {'name': 'Pizza', 'price': 10.99},
        {'name': 'Burger', 'price': 7.99},
         {'name': 'Salad', 'price': 6.99},
        {'name': 'Sushi', 'price': 15.99},
        {'name': 'Steak', 'price': 19.99},
        {'name': 'Tacos', 'price': 8.99},
        {'name': 'Ice Cream', 'price': 4.99},
        {'name': 'Sandwich', 'price': 5.99},
        {'name': 'Soup', 'price': 6.49},
    ]
    return render(request, 'menu.html', {'item': item})

# Create your views here.
