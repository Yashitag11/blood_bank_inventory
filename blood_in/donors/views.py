from django.shortcuts import render, redirect, get_object_or_404
from .models import Donor, MedicalInfo, FamilyDonationInfo
# Create your views here.
def login_view(request):
    if request.method == "POST":
        donor = Donor.objects.create(
            registration_no=request.POST.get('registration_no'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            dob=request.POST.get('dob'),
            age=request.POST.get('age'),
        )
        MedicalInfo.objects.create(
            donor=donor,
            blood_group=request.POST.get('blood_group'),
            medical_conditions = request.POST.get('medical_conditions')
        )
        FamilyDonationInfo.objects.create(
            donor=donor,
            father_blood_group=request.POST.get('father_blood_group'),
            mother_blood_group=request.POST.get('mother_blood_group'),
            last_donation_date=request.POST.get('last_donation_date'),
        )
        return redirect('success')
    return render(request, 'login.html')

def records_view(request):
    donors = Donor.objects.all()
    return render(request, 'records.html', {'donors': donors})

def success_view(request):
    return render(request, 'success.html')

def delete_view(request, pk):
    donor = get_object_or_404(Donor, registration_no=pk)
    donor.delete()
    return redirect('records')

def edit_view(request, pk):
    donor = get_object_or_404(Donor, registration_no=pk)
    medical = donor.medicalinfo
    family = donor.familydonationinfo

    if request.method == "POST":
        donor.first_name = request.POST.get('first_name')
        donor.last_name = request.POST.get('last_name')
        donor.email = request.POST.get('email')
        donor.phone = request.POST.get('phone')
        donor.age = request.POST.get('age')

        medical.blood_group = request.POST.get('blood_group')

        family.father_blood_group = request.POST.get('father_blood_group')
        family.mother_blood_group = request.POST.get('mother_blood_group')
        family.last_donation_date = request.POST.get('last_donation_date')

        donor.save()
        medical.save()
        family.save()

        return redirect('records')

    return render(request, 'edit.html', {
        'donor': donor,
        'medical': medical,
        'family': family
    })