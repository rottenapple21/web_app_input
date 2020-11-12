from .models import AddLink
from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

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

class AddLinkForm(forms.ModelForm):
    Nama = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nama Pengirim (ex : Susi Susanti)'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Pengirim (ex : kurasi@web.com)'}))
    Judul = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Judul Materi (ex : Ayo Belajar Perkalian)'}))
    Pelajaran = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Jenis Pelajaran (ex : Matematika, Biologi, Bahasa Inggris)'}))
    Kategori = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Kategori Materi (ex : Perkalian, Makhluk Hidup, Introduction)'}))
    Kelas = forms.ChoiceField(choices = PilihKelas)
    Link = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Tambahkan Link Materi'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('Nama', css_class='form-group col-md-6 mb-0'),
                Column('Email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Judul', css_class='form-group col-md-6 mb-0'),
                Column('Pelajaran', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('Kategori', css_class='form-group col-md-6 mb-0'),
                Column('Kelas', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'Link',
            Submit('submit', 'Kirim')
        )

    class Meta:
        model = AddLink
        fields = ['Nama', 'Email', 'Judul', 'Pelajaran', 'Kategori', 'Kelas', 'Link']
