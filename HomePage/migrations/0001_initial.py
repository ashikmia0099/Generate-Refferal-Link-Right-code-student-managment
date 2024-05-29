# Generated by Django 4.2.11 on 2024-05-25 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Deshboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer_Last_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institute_Logo', models.ImageField(blank=True, null=True, upload_to='HomePage/media/')),
                ('copyright_text', models.CharField(blank=True, max_length=500, null=True)),
                ('licence_number', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name': '3.Footer warning site',
                'verbose_name_plural': '3.Footer warning site',
            },
        ),
        migrations.CreateModel(
            name='Footer_other_detail_header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header_Name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': '1. Footer Other Detail Title',
                'verbose_name_plural': '1. Footer Other Detail Title',
            },
        ),
        migrations.CreateModel(
            name='Navbar_text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Latest Navbar News Text',
                'verbose_name_plural': 'Latest Navbar News Text',
            },
        ),
        migrations.CreateModel(
            name='Seminer_Image_Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seminer_image', models.ImageField(blank=True, default=' ', null=True, upload_to='HomePage/media/')),
                ('seminer_text', models.TextField(blank=True, default=' ', null=True)),
            ],
            options={
                'verbose_name': 'Set Home Page Seminer Image',
                'verbose_name_plural': 'Set Home Page Seminer Image',
            },
        ),
        migrations.CreateModel(
            name='Seminer_Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, default=' ', max_length=10, null=True)),
                ('month_Year', models.CharField(blank=True, default=' ', max_length=20, null=True)),
                ('seminer_subject', models.CharField(blank=True, default=' ', max_length=150, null=True)),
                ('seminer_time', models.CharField(blank=True, default=' ', max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Set Online Seminer Time',
                'verbose_name_plural': 'Set Online Seminer Time',
            },
        ),
        migrations.CreateModel(
            name='Header_li',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('List_Data', models.TextField(blank=True, max_length=300, null=True)),
                ('HeaderChoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HomePage.footer_other_detail_header')),
            ],
            options={
                'verbose_name': '2. Footer Other Detail Title Data',
                'verbose_name_plural': '2. Footer Other Detail Title Data',
            },
        ),
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_summery_text', models.TextField(blank=True, default=' ', null=True)),
                ('Category_image', models.ImageField(blank=True, default=' ', null=True, upload_to='Home_Page_Two/media/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='Deshboard.all_category_model')),
            ],
            options={
                'verbose_name': 'Category Page Top Data',
                'verbose_name_plural': 'Category Page Top Data',
            },
        ),
    ]
