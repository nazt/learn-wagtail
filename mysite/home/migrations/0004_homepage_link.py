# Generated by Django 3.2.6 on 2021-08-22 04:43

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='link',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]