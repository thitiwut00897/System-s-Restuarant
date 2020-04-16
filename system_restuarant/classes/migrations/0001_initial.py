# Generated by Django 3.0.4 on 2020-04-16 16:46

import classes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='uploads')),
                ('price', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[(classes.models.StateChoices['QUEUING'], 'Queuing'), (classes.models.StateChoices['DOING'], 'Doing'), (classes.models.StateChoices['DONE'], 'Done')], default=classes.models.StateChoices['QUEUING'], max_length=10)),
                ('total_price', models.FloatField(max_length=10)),
                ('date_time', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('faculty', models.CharField(max_length=50)),
                ('account_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='classes.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('picture_owner', models.ImageField(upload_to='uploads')),
                ('account_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='classes.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.AutoField(primary_key=True, serialize=False)),
                ('working_hours', models.TimeField(blank=True)),
                ('picture_restaurant', models.ImageField(upload_to='uploads')),
                ('restaurant_name', models.CharField(max_length=50)),
                ('type_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Type')),
                ('owner_account_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Order_List',
            fields=[
                ('list_no', models.AutoField(primary_key=True, serialize=False)),
                ('unit', models.IntegerField()),
                ('price', models.FloatField(max_length=50)),
                ('food_food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Food')),
                ('order_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Order')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant_restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Restaurant'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_account_account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Customer'),
        ),
    ]
