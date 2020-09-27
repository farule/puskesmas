from odoo import models, fields

class puskesmas_pasien(models.Model):
    _name = "puskesmas_pasien"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Record data pasien"
    _order = "nama_pasien asc"
    _rec_name = "nama_pasien"

    nama_pasien = fields.Char (string="Name", required=True)
    usia_pasien = fields.Integer (string="Usia")
    golongan_darah = fields.Selection([("a","A"), ("b", "B"), ("ab", "AB"), ("o", "O") ], string="Golongan Darah")
    notes = fields.Text (string="Notes")
    image = fields.Binary (string="Foto")
    mobile = fields.Integer(string="No Hp")
    jenis_kelamin = fields.Selection([("pria","Laki-laki"), ("perempuan", "Perempuan")], string="Jenis Kelamin")
    pekerjaan = fields.Selection([
        ('pelajar_mhs','Pelajar/Mahasiswa'),
        ('pegawai_negeri','Pegawai Negeri'),
        ('abri','ABRI'),
        ('swasta','Swasta'),
        ('lain','Lain-Lain'),
    ], string='Pekerjaan')
    tgl_lahir = fields.Date('Tanggal Lahir')
    kode = fields.Char(string='Kode', default='/')
    status = fields.Selection([
        ('lajang','Lajang'),
        ('menikah','Menikah'),
        ('duda','Duda'),
        ('janda','Janda'),
    ], string='Status')
