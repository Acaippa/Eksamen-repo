# Generated by Django 4.2.1 on 2023-05-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leverandor', models.CharField(max_length=20)),
                ('modell', models.CharField(max_length=20)),
                ('serienummer', models.IntegerField()),
                ('status', models.CharField(choices=[('ut', 'Utlånt'), ('iut', 'Ikke utlånt')], max_length=12)),
                ('notater', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
