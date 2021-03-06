# Generated by Django 3.1.7 on 2021-05-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210529_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('1', 'pending'), ('2', 'approve'), ('3', 'cancel')], default='pending', max_length=15),
        ),
        migrations.AlterField(
            model_name='room',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='room/'),
        ),
    ]
