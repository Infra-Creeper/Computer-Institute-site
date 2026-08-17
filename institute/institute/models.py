from decimal import Decimal
from uuid import uuid4

from django.conf import settings
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


    # Do not declare an inner Meta class here. Child models define their own
    # Meta classes, and this avoids Pylance's incompatible variable override
    # warning for nested Meta types.


class CourseCategory(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Course categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(TimeStampedModel):
    category = models.ForeignKey(
        CourseCategory,
        on_delete=models.PROTECT,
        related_name="courses",
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    short_description = models.TextField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/", blank=True, null=True)
    image_alt = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    batch_info = models.CharField(max_length=255, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("display_order", "title")
        indexes = [
            models.Index(fields=["is_active", "is_featured", "display_order"]),
            models.Index(fields=["category", "is_active"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def excerpt(self):
        return self.short_description or self.description[:180]

    @property
    def fee_display(self):
        return f"{self.fee:,.2f}"

    def get_absolute_url(self):
        return reverse("training:course-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class SyllabusModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="syllabus")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("display_order", "id")

    def __str__(self):
        return f"{self.course.title}: {self.title}"


class Notice(TimeStampedModel):
    title = models.CharField(max_length=220)
    slug = models.SlugField(max_length=240, unique=True, blank=True)
    content = models.TextField()
    attachment = models.FileField(
        upload_to="notice-attachments/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx", "jpg", "jpeg", "png"])],
    )
    published_at = models.DateTimeField(default=timezone.now, db_index=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ("-published_at", "-id")
        indexes = [models.Index(fields=["is_published", "-published_at"])]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def date(self):
        return self.published_at

    @property
    def excerpt(self):
        return self.content[:220]

    @property
    def attachment_url(self):
        return self.attachment.url if self.attachment else ""

    @property
    def is_recent(self):
        return self.published_at >= timezone.now() - timezone.timedelta(days=14)

    def get_absolute_url(self):
        return reverse("training:notice-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class BlogCategory(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Blog categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class BlogPost(TimeStampedModel):
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.PROTECT,
        related_name="posts",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        blank=True,
        null=True,
    )
    title = models.CharField(max_length=240)
    slug = models.SlugField(max_length=260, unique=True, blank=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="blog/", blank=True, null=True)
    featured_image_alt = models.CharField(max_length=255, blank=True)
    read_time = models.CharField(max_length=50, blank=True, default="5 min read")
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ("-published_at", "-id")
        indexes = [models.Index(fields=["is_published", "-published_at"])]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.is_published and self.published_at is None:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def featured_image_url(self):
        return self.featured_image.url if self.featured_image else ""

    def get_absolute_url(self):
        return reverse("training:blog-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class AdmissionApplication(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"
        OTHER = "other", "Other"
        PREFER_NOT_TO_SAY = "prefer_not_to_say", "Prefer not to say"

    class Category(models.TextChoices):
        ST = "ST", "ST"
        SC = "SC", "SC"
        OBC = "OBC", "OBC"
        IRDP = "IRDP", "IRDP"
        BPL = "BPL", "BPL"
        GENERAL = "General", "General"
        OTHER = "Other", "Other"

    class Status(models.TextChoices):
        SUBMITTED = "submitted", "Submitted"
        UNDER_REVIEW = "under_review", "Under review"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"
        WITHDRAWN = "withdrawn", "Withdrawn"

    reference_number = models.CharField(max_length=32, unique=True, editable=False, db_index=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name="admission_applications",
    )
    name = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120, blank=True)
    mother_name = models.CharField(max_length=120, blank=True)
    address = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=24, choices=Gender.choices)
    contact_no = models.CharField(max_length=25)
    nationality = models.CharField(max_length=80, default="Indian")
    category = models.CharField(max_length=10, choices=Category.choices)
    highest_qualification = models.CharField(max_length=200)
    document = models.FileField(
        upload_to="admission-documents/%Y/%m/",
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "jpg", "jpeg", "png"])],
    )
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SUBMITTED, db_index=True)

    # Required submission timestamp. It is generated once when the application is created.
    date_submitted = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-date_submitted", "-id")
        indexes = [
            models.Index(fields=["course", "-date_submitted"]),
            models.Index(fields=["status", "-date_submitted"]),
        ]

    def save(self, *args, **kwargs):
        if not self.reference_number:
            self.reference_number = f"APP-{timezone.now():%Y%m%d}-{uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return self.name

    @property
    def so(self):
        return self.father_name

    @property
    def do(self):
        return self.mother_name

    def __str__(self):
        return f"{self.reference_number} — {self.name}"


class ContactMessage(TimeStampedModel):
    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In progress"
        RESOLVED = "resolved", "Resolved"
        SPAM = "spam", "Spam"

    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW, db_index=True)
    responded_at = models.DateTimeField(blank=True, null=True)
    responded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="responded_contact_messages",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ("-created_at", "-id")

    def __str__(self):
        return f"{self.name} — {self.email}"


class InstituteProfile(TimeStampedModel):
    """Optional singleton-style content model for shared institute information."""

    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    logo = models.ImageField(upload_to="institute/", blank=True, null=True)
    about_content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Institute profile"
        verbose_name_plural = "Institute profiles"

    def __str__(self):
        return self.name
