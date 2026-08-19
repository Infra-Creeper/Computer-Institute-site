import uuid
from django.db import models
from django.core.validators import RegexValidator


class Admission(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    CATEGORY_CHOICES = [
        ('GEN', 'General'),
        ('OBC', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('EWS', 'EWS'),
        ('OTHER', 'Other'),
    ]

    phone_validator = RegexValidator(
        regex=r'^\+?\d{7,15}$',
        message="Enter a valid contact number (7-15 digits, optional leading +)."
    )

    ref_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        help_text="Auto-generated application reference number."
    )
    course_name = models.CharField(max_length=200)
    name = models.CharField(max_length=150)
    guardian = models.CharField(max_length=150, verbose_name="Guardian's Name")
    address = models.TextField()
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15, validators=[phone_validator])
    nationality = models.CharField(max_length=100, default="Indian")
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='GEN')
    highest_qualification = models.CharField(max_length=150)

    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']

    def save(self, *args, **kwargs):
        if not self.ref_id:
            self.ref_id = f"ADM-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ref_id} — {self.name}"


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email_or_phone = models.CharField(
        max_length=150,
        verbose_name="Email / Phone",
        help_text="Accepts either an email address or a phone number."
    )
    message = models.TextField()

    submitted_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.name} — {self.submitted_at.strftime('%Y-%m-%d')}"


class Notice(models.Model):
    number = models.PositiveIntegerField(
        unique=True,
        editable=False,
        help_text="Auto-incrementing notice number."
    )
    title = models.CharField(max_length=200)
    message = models.TextField()

    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-number']

    def save(self, *args, **kwargs):
        if not self.number:
            last = Notice.objects.order_by('-number').first()
            self.number = (last.number + 1) if last else 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"#{self.number} — {self.title}"