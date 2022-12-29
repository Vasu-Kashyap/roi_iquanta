# Generated by Django 4.1.2 on 2022-10-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fees', models.FloatField()),
                ('average', models.FloatField(blank=True, null=True)),
                ('median', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'College',
            },
        ),
    ]