# Generated by Django 4.2.6 on 2023-12-02 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_alter_moviles_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviles',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
