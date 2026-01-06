from django.shortcuts import render
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def become_client(request):
    return render(request, 'become_client.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Hier kun je de email versturen of opslaan in database
        # Voor nu: gewoon een success message
        messages.success(request, 'Bedankt voor uw bericht! We nemen zo snel mogelijk contact op.')
        
    return render(request, 'contact.html')

def room(request, pk):
    # Je oude room functie - indien je die nog nodig hebt
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'room.html', context)