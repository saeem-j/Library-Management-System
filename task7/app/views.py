from django.shortcuts import render

def hotels(request):
    room = [{"room_number": "101", "room_type": "Deluxe", "price": "$100"},
            {"room_number": "102", "room_type": "Standard", "price": "$80"},
            {"room_number": "103", "room_type": "Suite", "price": "$150"},
            {"room_number": "104", "room_type": "Deluxe", "price": "$120"},
            {"room_number": "105", "room_type": "Standard", "price": "$90"}]
    
    return render(request,'hotels.html', {"room": room})

# Create your views here.
