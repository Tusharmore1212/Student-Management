# Generated by Django 5.0.6 on 2024-06-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_student_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='static/img')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
