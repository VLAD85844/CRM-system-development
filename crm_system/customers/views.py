from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm
from leads.models import Lead

@login_required
def customer_list(request):
    customers = Customer.objects.select_related('lead').all()
    return render(request, 'customers/customers-list.html', {'customers': customers})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect(f'/customers/{customer.pk}/')
    else:
        form = CustomerForm()
    return render(request, 'customers/customers-create.html', {'form': form})

@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer.objects.select_related('lead'), pk=pk)
    return render(request, 'customers/customers-detail.html', {'object': customer})

@login_required
def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect(f'/customers/{customer.pk}/')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customers-edit.html', {'form': form, 'object': customer})

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/customers/')
    return render(request, 'customers/customers-delete.html', {'object': customer})