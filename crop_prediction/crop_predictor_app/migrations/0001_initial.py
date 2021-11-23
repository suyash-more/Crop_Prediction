# Generated by Django 3.2.9 on 2021-11-23 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CropDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('nitrogen_content', models.IntegerField(default=0, null=True)),
                ('phosphorus_content', models.IntegerField(default=0, null=True)),
                ('potassium_content', models.IntegerField(default=0, null=True)),
                ('temperature', models.IntegerField(default=0, null=True)),
                ('humidity', models.IntegerField(default=0, null=True)),
                ('ph', models.IntegerField(default=0, null=True)),
                ('rainfall', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]