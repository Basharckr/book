# Generated by Django 3.2.5 on 2021-07-13 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=150)),
                ('count', models.IntegerField()),
                ('borrow_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
