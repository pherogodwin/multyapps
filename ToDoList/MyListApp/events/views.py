# events/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Seat, Booking
from .forms import BookingForm
from django.core.mail import send_mail

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    seats = Seat.objects.filter(event=event, is_booked=False)
    return render(request, 'events/event_detail.html', {'event': event, 'seats': seats})

def book_ticket(request, seat_id):
    seat = get_object_or_404(Seat, id=seat_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.seat = seat
            booking.event = seat.event
            booking.save()
            seat.is_booked = True
            seat.save()

            # Send email
            send_mail(
                'Ticket Confirmation',
                f'Thank you for booking a ticket for {seat.event.name}. Your seat number is {seat.seat_number}.',
                'from@example.com',
                [booking.user_email],
                fail_silently=False,
            )

            return redirect('events:booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'events/book_ticket.html', {'form': form, 'seat': seat})

def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'events/booking_confirmation.html', {'booking': booking})
