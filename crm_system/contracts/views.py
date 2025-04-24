from .models import Contract
from .forms import ContractForm
from customers.models import Customer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.utils import timezone

@login_required
@permission_required('contracts.can_manage_contracts', raise_exception=True)
def contract_list(request):
    contracts = Contract.objects.select_related('customer', 'product').all()
    return render(request, 'contracts/contracts-list.html', {'contracts': contracts})


@login_required
@permission_required('contracts.can_manage_contracts', raise_exception=True)
def contract_create(request):
    customer_id = request.GET.get('customer_id')

    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.manager = request.user
            contract.save()
            return redirect(f'/contracts/{contract.pk}/')
    else:
        initial = {'signing_date': timezone.now().date()}
        if customer_id:
            initial['customer'] = get_object_or_404(Customer, pk=customer_id)
        form = ContractForm(initial=initial)

    return render(request, 'contracts/contracts-create.html', {'form': form})


@login_required
def contract_detail(request, pk):
    contract = get_object_or_404(
        Contract.objects.select_related('customer', 'product', 'manager'),
        pk=pk
    )
    return render(request, 'contracts/contracts-detail.html', {'object': contract})


@login_required
@permission_required('contracts.can_manage_contracts', raise_exception=True)
def contract_edit(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, request.FILES, instance=contract)
        if form.is_valid():
            form.save()
            return redirect(f'/contracts/{contract.pk}/')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'contracts/contracts-edit.html', {'form': form, 'object': contract})


@login_required
@permission_required('contracts.can_manage_contracts', raise_exception=True)
def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        return redirect('/contracts/')
    return render(request, 'contracts/contracts-delete.html', {'object': contract})