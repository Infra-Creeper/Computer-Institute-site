from django.db import migrations, models
from django.utils.text import slugify


def populate_notice_slugs(apps, schema_editor):
    Notice = apps.get_model("home", "Notice")
    for notice in Notice.objects.order_by("number"):
        notice.slug = f"{slugify(notice.title)}-{notice.number}"
        notice.save(update_fields=["slug"])


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_admission_contact_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            'DROP INDEX IF EXISTS "home_notice_slug_f6f6c921_like"',
            migrations.RunSQL.noop,
        ),
        migrations.AddField(
            model_name="notice",
            name="slug",
            field=models.SlugField(blank=True, db_index=False, max_length=220, null=True),
        ),
        migrations.RunPython(populate_notice_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="notice",
            name="slug",
            field=models.SlugField(db_index=False, editable=False, max_length=220, unique=True),
        ),
    ]
