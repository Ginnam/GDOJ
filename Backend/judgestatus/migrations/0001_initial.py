# Generated by Django 2.1.5 on 2019-03-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JudgeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('oj', models.CharField(default='LPOJ', max_length=50)),
                ('problem', models.CharField(max_length=50)),
                ('result', models.IntegerField()),
                ('time', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('length', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('submittime', models.DateTimeField(auto_now=True)),
                ('judger', models.CharField(max_length=50)),
                ('contest', models.IntegerField()),
                ('code', models.TextField()),
                ('testcase', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]
