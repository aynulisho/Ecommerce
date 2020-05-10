# Generated by Django 2.2 on 2020-05-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=100)),
                ('catagory', models.CharField(max_length=10)),
                ('buying_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(height_field=520, upload_to='product', width_field=520)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
