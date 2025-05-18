from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send an email
            send_mail(
                f'Message from {name}',
                message,
                email,
                ['rasha172019@gmail.com'],  # my email
                fail_silently=False,
            )

            return redirect('success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def success_view(request):
    return render(request, 'contact/success.html')
