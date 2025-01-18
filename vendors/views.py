from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from vendors.tests import is_vendor
from feed.tests import identity_verified, identity_really_verified

def video(request, username):
    from .models import VendorProfile
    from django.shortcuts import redirect
    from django.contrib import messages
    from security.apis import get_client_ip, check_raw_ip_risk
    if not request.COOKIES.get('age_verified', None) or check_raw_ip_risk(get_client_ip(request), True, False):
        messages.warning(request, 'You may not visit this link, as per the site policies.')
        return redirect(reverse('misc:terms'))
    profile = VendorProfile.objects.filter(user__profile__name=username).first()
    return redirect('/' if not profile.video_link else profile.video_link)

def content(request, username):
    from .models import VendorProfile
    from django.shortcuts import redirect
    from django.contrib import messages
    from security.apis import get_client_ip, check_raw_ip_risk
    if not request.COOKIES.get('age_verified', None) or check_raw_ip_risk(get_client_ip(request), True, False):
        messages.warning(request, 'You may not visit this link, as per the site policies.')
        return redirect(reverse('misc:terms'))
    profile = VendorProfile.objects.filter(user__profile__name=username).first()
    return redirect('/' if not profile.content_link else profile.content_link)

@login_required
@user_passes_test(identity_verified, login_url='/verify/', redirect_field_name='next')
@user_passes_test(is_vendor)
def send_bitcoin(request):
    from .models import VendorPaymentsProfile
    from django.shortcuts import render
    profile, created = VendorPaymentsProfile.objects.get_or_create(vendor=request.user)
    return render(request, 'vendors/send_bitcoin.html', {'title': 'Crypto', 'info': profile.get_crypto_balances()})


@login_required
@user_passes_test(identity_really_verified, login_url='/verify/', redirect_field_name='next')
def onboarding(request):
    from django.shortcuts import redirect
    from django.urls import reverse
    from payments.models import VendorProfile
    if not hasattr(request.user, 'vendor_profile'):
        v = VendorProfile.objects.create(user=request.user)
        v.save()
        request.user.profile.vendor = True
        request.user.profile.save()
    return redirect(reverse('feed:profile', kwargs={'username': request.user.username}))

@login_required
@user_passes_test(identity_really_verified, login_url='/verify/', redirect_field_name='next')
def vendor_preferences(request):
    from django.shortcuts import redirect, render
    from django.urls import reverse
    from payments.models import VendorPaymentsProfile
    from .forms import VendorProfileUpdateForm
    from .models import VendorProfile
    from django.contrib import messages
    v, created = VendorProfile.objects.get_or_create(user=request.user)
    v.save()
    form = VendorProfileUpdateForm(instance=v)
    if request.method == 'POST':
        form = VendorProfileUpdateForm(request.POST, instance=request.user.vendor_profile)
        if form.is_valid():
            form.instance.user = request.user
            from payments.apis import validate_address
            accepted = True
            try:
                if form.cleaned_data.get('payout_address') and not validate_address(form.cleaned_data.get('payout_address'), form.cleaned_data.get('payout_currency')):
                    form.instance.payout_address = ''
                    messages.warning(request, 'This crypto address could not be accepted. Please check the address and the currency.')
                    accepted = False
            except:
                form.instance.payout_address = ''
                messages.warning(request, 'This crypto address could not be accepted. Please check the address and the currency.')
                accepted = False
            try:
                if form.cleaned_data.get('bitcoin_address') and not validate_address(form.cleaned_data.get('bitcoin_address'), 'BTC'):
                    form.instance.bitcoin_address = ''
                    messages.warning(request, 'This bitcoin address could not be accepted. Please check the address and the currency.')
            except:
                form.instance.bitcoin_address = ''
                messages.warning(request, 'This bitcoin address could not be accepted. Please check the address and the currency.')
            try:
                if form.cleaned_data.get('ethereum_address') and not validate_address(form.cleaned_data.get('ethereum_address'), 'ETH'):
                    form.instance.ethereum_address = ''
                    messages.warning(request, 'This ethereum address could not be accepted. Please check the address and the currency.')
            except:
                form.instance.ethereum_address = ''
                messages.warning(request, 'This ethereum address could not be accepted. Please check the address and the currency.')
            if accepted:
                p = form.save()
                p.user.profile.vendor = True
                p.user.profile.save()
                messages.success(request, 'Vendor profile updated.')
                return redirect(reverse('go:go'))
    from django.conf import settings
    return render(request, 'vendors/vendor_preferences.html', {'title': 'Vendor Preferences','form': form, 'payment_processor': settings.PAYMENT_PROCESSOR})
