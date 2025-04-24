from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Advertisement
from .forms import AdvertisementForm

@login_required
@permission_required('ads.view_advertisement', raise_exception=True)
def ad_list(request):
    ads = Advertisement.objects.select_related('product').all()
    return render(request, 'ads/ads-list.html', {'ads': ads})

@login_required
@permission_required('ads.add_advertisement', raise_exception=True)
def ad_create(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            ad = form.save()
            return redirect(f'/ads/{ad.pk}/')
    else:
        form = AdvertisementForm()
    return render(request, 'ads/ads-create.html', {'form': form})

@login_required
def ad_detail(request, pk):
    ad = get_object_or_404(Advertisement.objects.select_related('product'), pk=pk)
    return render(request, 'ads/ads-detail.html', {'object': ad})

@login_required
@permission_required('ads.change_advertisement', raise_exception=True)
def ad_edit(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect(f'/ads/{ad.pk}/')
    else:
        form = AdvertisementForm(instance=ad)
    return render(request, 'ads/ads-edit.html', {'form': form, 'object': ad})

@login_required
@permission_required('ads.delete_advertisement', raise_exception=True)
def ad_delete(request, pk):
    ad = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        ad.delete()
        return redirect('/ads/')
    return render(request, 'ads/ads-delete.html', {'object': ad})

@login_required
def ad_statistic(request):
    ads = Advertisement.objects.prefetch_related('product').all()
    return render(request, 'ads/ads-statistic.html', {'ads': ads})