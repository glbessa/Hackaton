# Generated by Django 3.2.9 on 2022-11-05 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passenger_id', models.CharField(max_length=10)),
                ('passenger_name', models.CharField(max_length=50)),
                ('passenger_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('passenger_lon', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.IntegerField(primary_key=True, serialize=False)),
                ('route_name', models.CharField(max_length=100)),
                ('route_est_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('passenger_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bustracker.passenger')),
                ('driver_id', models.CharField(max_length=10)),
                ('driver_name', models.CharField(max_length=50)),
            ],
            bases=('bustracker.passenger',),
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('stop_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stop_name', models.CharField(max_length=100)),
                ('stop_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('stop_lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('stop_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bustracker.route')),
            ],
        ),
        migrations.CreateModel(
            name='RouteStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_order', models.IntegerField()),
                ('route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bustracker.route')),
                ('stop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bustracker.stop')),
            ],
        ),
        migrations.AddField(
            model_name='passenger',
            name='passenger_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bustracker.route'),
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_id', models.CharField(max_length=10)),
                ('bus_lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('bus_long', models.DecimalField(decimal_places=6, max_digits=9)),
                ('bus_speed', models.DecimalField(decimal_places=6, max_digits=9)),
                ('bus_time', models.TimeField()),
                ('bus_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bustracker.route')),
            ],
        ),
    ]
