# Generated by Django 2.0.5 on 2019-03-27 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20190325_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='objname',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
