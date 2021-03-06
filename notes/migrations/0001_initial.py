# Generated by Django 4.0.4 on 2022-04-26 16:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(default='General', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=256)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('created_on', models.DateField()),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.tags')),
            ],
        ),
    ]
