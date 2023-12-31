# Generated by Django 2.2.18 on 2022-06-14 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Recived', 'Recived'), ('Reject', 'Reject')], max_length=200, null=True)),
                ('george', models.IntegerField(blank=True, default=0, null=True)),
                ('castel', models.IntegerField(blank=True, default=0, null=True)),
                ('doppel', models.IntegerField(blank=True, default=0, null=True)),
                ('senq', models.IntegerField(blank=True, default=0, null=True)),
                ('Agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.Agent')),
                ('Store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.Company_Store')),
            ],
        ),
        migrations.CreateModel(
            name='Agent_Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Store_Name', models.CharField(max_length=200, null=True)),
                ('Location', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Compan_name', models.CharField(max_length=200, null=True)),
                ('phone1', models.CharField(max_length=200, null=True)),
                ('phone2', models.CharField(max_length=200, null=True)),
                ('Address', models.CharField(max_length=200, null=True)),
                ('House_No', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Profile/')),
                ('TIN_NO', models.CharField(max_length=500, null=True)),
                ('License', models.FileField(blank=True, null=True, upload_to='License')),
                ('Marchent_id', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.Agent')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vichel_name', models.CharField(max_length=100, null=True)),
                ('vichel_type', models.CharField(choices=[('Fetch track:', 'Fetch track'), ('Distribution track', 'Distribution track')], max_length=200, null=True)),
                ('vichel_No', models.CharField(max_length=200, null=True)),
                ('vichel_pic', models.ImageField(blank=True, null=True, upload_to='vichel_pic/')),
                ('Agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Product_in_Agent_Stor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('castel', 'castel'), ('senq', 'senq'), ('doppel', 'doppel'), ('george', 'george')], max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('quantity', models.IntegerField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.Agent')),
                ('Store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Agent.Agent_Store')),
            ],
        ),
        migrations.CreateModel(
            name='Notfifcation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('mssg', models.TextField(blank=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Agent')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agent.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('on_duty', 'on_duty'), ('on_garage', 'on_garage'), ('on_wating', 'on_wating')], default='on_wating', max_length=200, null=True)),
                ('Full_name', models.CharField(max_length=200, null=True)),
                ('phone1', models.CharField(max_length=200, null=True)),
                ('salary', models.CharField(max_length=500, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Profile/')),
                ('Drive_license', models.FileField(blank=True, null=True, upload_to='License')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Agent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.Agent')),
                ('vehicle', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Agent.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Customers_message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(blank=True, max_length=200, null=True)),
                ('mssg', models.TextField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Agent_Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Total_Amount', models.FloatField(null=True)),
                ('Paid_status', models.CharField(choices=[('Paid', 'Paid'), ('Not Paid', 'Not Paid')], max_length=200, null=True)),
                ('TransactionCode', models.CharField(max_length=200, null=True)),
                ('MarchentId', models.CharField(max_length=200, null=True)),
                ('scheduled_for', models.DateField(blank=True, null=True)),
                ('scheduled_to', models.DateField(blank=True, null=True)),
                ('Agent_order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Agent.Agent_order')),
            ],
        ),
        migrations.CreateModel(
            name='Agent_finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone1', models.CharField(max_length=200, null=True)),
                ('Adderes', models.CharField(max_length=200, null=True)),
                ('about', models.TextField(blank=True, max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Telegram', models.CharField(max_length=200, null=True)),
                ('facebook', models.CharField(max_length=200, null=True)),
                ('instagrm', models.CharField(max_length=200, null=True)),
                ('Agent', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.Agent')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
