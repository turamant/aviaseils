from django.shortcuts import render, redirect, get_object_or_404

from content.forms import CompanyForm
from content.models import Company


# Create your views here.


def index(request):
    return render(request, 'content/index.html')


def list_company(request):
    companies = Company.objects.all()
    context = {'companies': companies}
    return render(request, 'content/list_company.html', context)


def get_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    context = {'company': company}
    return render(request, 'content/company.html', context)


def create_company(request):
    form = CompanyForm()
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form
    }
    return render(request, "content/company_create.html", context)


def update_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    form = CompanyForm(instance=company)
    if request.method == "POST":
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {
        "form": form,
    }
    return render(request, "content/company_update.html", context)


def delete_company(request, pk):
    company = get_object_or_404(Company, id=pk)
    if request.method == "POST":
        company.delete()
        return redirect("/")
    return render(request, "content/company_delete.html", {'company': company})
