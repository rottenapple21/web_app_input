from django.db import models
from django import forms

PilihKelas = (
    ('', 'Pilih Kelas...'),
    ('0', 'Lain-lain'),
    ('1', 'Satu'),
    ('2', 'Dua'),
    ('3', 'Tiga'),
    ('4', 'Empat'),
    ('5', 'Lima'),
    ('6', 'Enam'),
)

class AddLink(models.Model):
    Nama = models.CharField(max_length = 50)
    Email = models.EmailField()
    Judul = models.CharField(max_length = 50)
    Kategori = models.CharField(max_length = 50)
    Pelajaran = models.CharField(max_length = 50, null=True)
    Kelas = models.CharField(max_length = 50, choices = PilihKelas)
    Link = models.CharField(max_length = 500)

    #def __str__(self):
        #return self.Kelas
