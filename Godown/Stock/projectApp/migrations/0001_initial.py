# Generated by Django 2.2.6 on 2020-05-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desktop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to get purchased'), ('SOLD', 'Item Sold'), ('Restocking', 'item restocking in Few days')], default='SOLD', max_length=10)),
                ('Issues', models.CharField(default='No  issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to get purchased'), ('SOLD', 'Item Sold'), ('Restocking', 'item restocking in Few days')], default='SOLD', max_length=10)),
                ('Issues', models.CharField(default='No  issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('AVAILABLE', 'Item ready to get purchased'), ('SOLD', 'Item Sold'), ('Restocking', 'item restocking in Few days')], default='SOLD', max_length=10)),
                ('Issues', models.CharField(default='No  issues', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]