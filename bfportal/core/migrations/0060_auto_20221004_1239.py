# Generated by Django 3.2.12 on 2022-10-04 12:39

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0059_auto_20221004_1127"),
    ]

    operations = [
        migrations.AddField(
            model_name="experiencescategory",
            name="meta_description",
            field=models.TextField(
                blank=True,
                help_text="If set this description is displayed in embeds",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="experiencescategory",
            name="meta_image",
            field=models.URLField(
                blank=True,
                help_text="If set this image is displayed in embeds. Recommend size 1200x630px",
                null=True,
                validators=[core.models.validate_image_link],
            ),
        ),
        migrations.AddField(
            model_name="experiencescategory",
            name="meta_title",
            field=models.CharField(
                blank=True,
                help_text="If set this title is displayed in embeds",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subcategory",
            name="meta_description",
            field=models.TextField(
                blank=True,
                help_text="If set this description is displayed in embeds",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="subcategory",
            name="meta_image",
            field=models.URLField(
                blank=True,
                help_text="If set this image is displayed in embeds. Recommend size 1200x630px",
                null=True,
                validators=[core.models.validate_image_link],
            ),
        ),
        migrations.AddField(
            model_name="subcategory",
            name="meta_title",
            field=models.CharField(
                blank=True,
                help_text="If set this title is displayed in embeds",
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="blogpage",
            name="meta_image",
            field=models.URLField(
                blank=True,
                help_text="If set this image is displayed in embeds. Recommend size 1200x630px",
                null=True,
                validators=[core.models.validate_image_link],
            ),
        ),
        migrations.AlterField(
            model_name="experiencepage",
            name="meta_image",
            field=models.URLField(
                blank=True,
                help_text="If set this image is displayed in embeds. Recommend size 1200x630px",
                null=True,
                validators=[core.models.validate_image_link],
            ),
        ),
        migrations.AlterField(
            model_name="experiencespage",
            name="meta_image",
            field=models.URLField(
                blank=True,
                help_text="If set this image is displayed in embeds. Recommend size 1200x630px",
                null=True,
                validators=[core.models.validate_image_link],
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="meta_image",
            field=models.URLField(
                blank=True,
                help_text="If set this image is displayed in embeds. Recommend size 1200x630px",
                null=True,
                validators=[core.models.validate_image_link],
            ),
        ),
        migrations.AlterField(
            model_name="profilepage",
            name="meta_image",
            field=models.URLField(
                blank=True,
                help_text="If set this image is displayed in embeds. Recommend size 1200x630px",
                null=True,
                validators=[core.models.validate_image_link],
            ),
        ),
    ]
