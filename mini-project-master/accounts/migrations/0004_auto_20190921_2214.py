# Generated by Django 2.2.4 on 2019-09-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190920_1900'),
    ]
'''
    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.IntegerField()),
                ('addr', models.CharField(max_length=50)),
                ('id_p', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=2)),
                ('ht', models.IntegerField()),
                ('wt', models.IntegerField()),
                ('med', models.CharField(max_length=50)),
                ('pass1', models.CharField(max_length=20)),
                ('pass2', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]
'''