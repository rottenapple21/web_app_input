# Generated by Django 3.1.2 on 2020-11-02 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Judul', models.CharField(max_length=50)),
                ('Kategori', models.CharField(max_length=50)),
                ('Kelas', models.CharField(choices=[('', 'Pilih Kelas...'), ('1', 'Satu'), ('2', 'Dua'), ('3', 'Tiga'), ('4', 'Empat'), ('5', 'Lima'), ('6', 'Enam')], max_length=50)),
                ('Link', models.CharField(max_length=300)),
            ],
        ),
    ]
