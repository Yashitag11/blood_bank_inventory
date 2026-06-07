from django.db import models
# Donor Personal Info
class Donor(models.Model):
    registration_no = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return self.first_name
    class Meta:
        db_table = 'donor_info'

# Medical Info
class MedicalInfo(models.Model):
    donor = models.OneToOneField(Donor, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    medical_conditions = models.TextField(
        blank=True,
        null=True,
        help_text="Enter any diseases or medical history"
    )

    def __str__(self):
        return self.donor.first_name
    
# Parents + Donation Info
class FamilyDonationInfo(models.Model):
    donor = models.OneToOneField(Donor, on_delete=models.CASCADE)
    father_blood_group = models.CharField(max_length=5)
    mother_blood_group = models.CharField(max_length=5)
    last_donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.donor.first_name
    class Meta:
        db_table = 'family_info'