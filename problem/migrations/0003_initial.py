# Generated by Django 4.0.5 on 2022-06-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('problem', '0002_delete_outputs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outputs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op', models.CharField(max_length=1000)),
            ],
        ),
    ]