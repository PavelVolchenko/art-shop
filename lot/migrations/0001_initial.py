# Generated by Django 4.0 on 2023-02-05 00:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='lot/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
