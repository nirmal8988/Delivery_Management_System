# Generated by Django 5.0.6 on 2024-06-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vortex_logistics_app', '0002_deliverycharge'),
    ]

    operations = [
        migrations.CreateModel(
            name='username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]
