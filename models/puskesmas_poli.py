from odoo import models, fields

class puskesmas_poli(models.Model):
    _name = "puskesmas_poli"
    _description = "Record data poli"
    _order = "nama_poli asc"
    _rec_name = "nama_poli"

    nama_poli = fields.Char (string="Nama Poli", required=True)
    kode = fields.Char (string="Kode Poli", required=True)