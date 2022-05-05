# Generated by Django 4.0.4 on 2022-05-05 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('credits', models.PositiveSmallIntegerField()),
                ('teacher', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveSmallIntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='M', max_length=1)),
                ('is_active', models.BooleanField(default=True)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment.degree')),
            ],
        ),
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managment.student')),
            ],
        ),
    ]
