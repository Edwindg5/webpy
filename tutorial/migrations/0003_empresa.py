# Generated by Django 4.2.18 on 2025-02-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0002_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
