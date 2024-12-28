from django.shortcuts import render
from .forms import SubscriptionForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'newsletter/subscribe_success.html')
    else:
        form = SubscriptionForm()
    return render(request, 'newsletter/subscribe.html', {'form': form})
