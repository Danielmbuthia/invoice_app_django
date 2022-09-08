# Generated by Django 4.1 on 2022-09-06 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_rename_tag_invoice_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='tags',
        ),
        migrations.AddField(
            model_name='invoice',
            name='avatar',
            field=models.ImageField(default='images/avatar.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='invoice',
            name='company_logo',
            field=models.ImageField(default='images/no_photo.png', upload_to=''),
        ),
    ]
