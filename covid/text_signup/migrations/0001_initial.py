# Generated by Django 3.0.8 on 2020-07-10 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_county', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_email_address', models.CharField(max_length=256)),
                ('t_phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_state', models.CharField(max_length=2)),
                ('t_state', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='RecipientSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text_signup.County')),
                ('n_recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text_signup.Recipient')),
            ],
        ),
        migrations.AddField(
            model_name='county',
            name='n_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='text_signup.State'),
        ),
    ]