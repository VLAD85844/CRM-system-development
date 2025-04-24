from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lead
from .forms import LeadForm

@login_required
def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/leads-list.html', {'leads': leads})

@login_required
def lead_create(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            return redirect(f'/leads/{lead.pk}/')
    else:
        form = LeadForm()
    return render(request, 'leads/leads-create.html', {'form': form})

@login_required
def lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads/leads-detail.html', {'object': lead})

@login_required
def lead_edit(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect(f'/leads/{lead.pk}/')
    else:
        form = LeadForm(instance=lead)
    return render(request, 'leads/leads-edit.html', {'form': form, 'object': lead})

@login_required
def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('/leads/')
    return render(request, 'leads/leads-delete.html', {'object': lead})