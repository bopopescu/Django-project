# Generated by Django 2.2.4 on 2019-10-02 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0004_comment_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='BeautySalon',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.Object')),
                ('is_hair_salon', models.BooleanField(default=False)),
                ('is_laser_epilation', models.BooleanField(default=False)),
            ],
            bases=('objects.object',),
        ),
        migrations.CreateModel(
            name='CarService',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.Object')),
                ('is_parts_clients', models.BooleanField(default=False)),
            ],
            bases=('objects.object',),
        ),
        migrations.CreateModel(
            name='CarWash',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.Object')),
                ('is_external_cleaning', models.BooleanField(default=False)),
                ('is_internal_cleaning', models.BooleanField(default=False)),
                ('is_engine_cleaning', models.BooleanField(default=False)),
            ],
            bases=('objects.object',),
        ),
        migrations.CreateModel(
            name='FastFood',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.Object')),
                ('is_pizza', models.BooleanField(default=False)),
                ('is_duner', models.BooleanField(default=False)),
                ('is_seats', models.BooleanField(default=False)),
            ],
            bases=('objects.object',),
        ),
        migrations.CreateModel(
            name='Fun',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.Object')),
                ('is_working_weekend', models.BooleanField(default=False)),
                ('is_kids_suitable', models.BooleanField(default=False)),
            ],
            bases=('objects.object',),
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.Object')),
                ('is_working_weekend', models.BooleanField(default=False)),
            ],
            bases=('objects.object',),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.Object')),
                ('seats', models.IntegerField()),
                ('bulgarian_kitchen', models.BooleanField(default=False)),
                ('italian_kitchen', models.BooleanField(default=False)),
                ('french_kitchen', models.BooleanField(default=False)),
                ('is_garden', models.BooleanField(default=False)),
                ('is_playground', models.BooleanField(default=False)),
            ],
            bases=('objects.object',),
        ),
        migrations.CreateModel(
            name='SportFitness',
            fields=[
                ('object_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='objects.Object')),
                ('is_fitness_trainer', models.BooleanField(default=False)),
            ],
            bases=('objects.object',),
        ),
        migrations.RemoveField(
            model_name='object',
            name='category',
        ),
    ]