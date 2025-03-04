# Generated by Django 3.2.8 on 2021-12-13 10:00

import datetime
from django.db import migrations, models
import django.db.models.deletion
import member.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=150, unique=True)),
                ('Password', models.CharField(max_length=150)),
                ('Username', models.CharField(max_length=150)),
                ('Name', models.CharField(max_length=150)),
                ('DateOfBirth', models.DateField()),
                ('Age', models.IntegerField()),
                ('District', models.CharField(max_length=150)),
                ('State', models.CharField(max_length=150)),
                ('Occupation', models.CharField(max_length=150)),
                ('About', models.CharField(max_length=150)),
                ('Gender', models.CharField(max_length=1)),
                ('MaritalStatus', models.CharField(max_length=150)),
                ('UserLevel', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'login_person',
            },
        ),
        migrations.CreateModel(
            name='Plants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pictures', models.ImageField(upload_to='uploads/')),
                ('Species', models.CharField(max_length=150)),
                ('Types', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'Plants',
            },
        ),
        migrations.CreateModel(
            name='PlantTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PlantTagName', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'PlantTag',
            },
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Detail', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'SensorData',
            },
        ),
        migrations.CreateModel(
            name='SoilTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoilTagName', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'SoilTag',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('ranking', models.FloatField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to=member.models.Users.upload_photo)),
                ('resume', models.ImageField(blank=True, null=True, upload_to=member.models.Users.upload_file)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member1', to='member.person')),
                ('member2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member2', to='member.person')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('sender', models.CharField(max_length=255)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.room')),
            ],
        ),
        migrations.CreateModel(
            name='MemberRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to='member.person')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to='member.person')),
            ],
            options={
                'unique_together': {('to_user', 'from_user')},
            },
        ),
        migrations.CreateModel(
            name='Memberlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatRoom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.room')),
                ('from_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_person', to='member.person')),
                ('to_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_person', to='member.person')),
            ],
            options={
                'unique_together': {('from_person', 'to_person')},
            },
        ),
    ]
