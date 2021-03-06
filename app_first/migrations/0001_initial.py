# Generated by Django 2.2 on 2020-04-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adres', models.CharField(db_index=True, max_length=150)),
                ('number_phon', models.CharField(max_length=150)),
                ('x_re', models.FloatField(default=0)),
                ('y_re', models.FloatField(default=0)),
                ('start', models.CharField(max_length=150)),
                ('stop', models.CharField(max_length=150)),
            ],
        ),
    ]
