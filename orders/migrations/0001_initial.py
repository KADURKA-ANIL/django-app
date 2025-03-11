# Generated by Django 4.2.11 on 2025-03-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
            options={
                'db_table': 'orders',
                'ordering': ['price'],
            },
        ),
    ]
