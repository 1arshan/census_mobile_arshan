from django.db import models


class State(models.Model):
    state_name = models.CharField(max_length=40, unique=True)
    def __str__(self):
        return f'{self.state_name}'


class District(models.Model):
    state_id = models.ForeignKey(State, on_delete=models.PROTECT)
    district_name = models.CharField(max_length=40)  # TODO: add uniqueness of someform in this
    def __str__(self):
        return f'State:{self.state_id}; District: {self.district_name}'

SEX_CHOICES = (
    ("1", "Male"),
    ("2", "Female"),
    ("3", "Prefer Not To Say"),
)


def renaming_uploaded_file1(instance, filename):
    return "profile_pic/" + str(instance.name) + "_" + str(instance.dob)+"_"+filename


class Child(models.Model):
    name = models.CharField(max_length=60)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    dob = models.DateField()
    father_name = models.CharField(max_length=60)
    mother_name = models.CharField(max_length=60)
    district_id = models.ForeignKey(District, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to=renaming_uploaded_file1, blank=True)

def renaming_uploaded_file2(instance, filename):
    return "photo/" + str(instance.imageName) + "_" + str(instance.mimeType)+"_"+filename


class File(models.Model):
    imageName=models.CharField(max_length=50)
    mimeType=models.CharField(max_length=50)
    photo=models.ImageField(upload_to=renaming_uploaded_file2, blank=True)