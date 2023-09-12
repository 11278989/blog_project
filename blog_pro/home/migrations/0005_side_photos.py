# Generated by Django 4.2.4 on 2023-08-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_side_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='side_photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='picture')),
                ('date', models.DateField()),
            ],
        ),
    ]