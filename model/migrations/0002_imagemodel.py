# Generated by Django 2.0.5 on 2019-03-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='images/None/no-img.jpg', upload_to='images/')),
            ],
        ),
    ]
