# Generated by Django 3.2.15 on 2022-08-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='gallery')),
                ('desc', models.TextField()),
                ('mrp', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
    ]