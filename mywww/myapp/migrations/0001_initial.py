# Generated by Django 2.1.7 on 2019-02-21 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.URLField(null=True)),
                ('website', models.URLField(null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Category')),
            ],
        ),
    ]
