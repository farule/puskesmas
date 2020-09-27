from odoo import models, fields, api
# from odoo.exceptions import Warning
# import unicodedata

class puskesmas_pendaftaran(models.Model):
    _name = "puskesmas_pendaftaran"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Record Pendaftaran"
    _order = "name desc"
    _inherit = "res.partner"
    _rec_name = "name_seq"

    

    #name_seq = fields.Char(string='Nomor Pendaftaran', required=True, copy=False, Index=True, default=lambda self: _('New'))
    name_seq = fields.Char(String= 'Nomor')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'Cancelled'),
        ('done', 'Done')], string="Status", default="draft")
    pasien_id = fields.Many2one('puskesmas_pasien', string='Nama Pasien')
    tgl_pendaftaran = fields.Datetime(string='Tanggal', default=fields.Datetime.now())
    note = fields.Html(string='Note')  
    dokter = fields.Char(string="Nama Dokter")
    poli_id = fields.Many2one('puskesmas_poli', string='Poli yang Dituju')

    #@api.model
    #def create(self, vals):
     #   if vals.get('name_seq', _('New')) == _('New'):
     #       vals['name_seq'] = self.env['ir.sequence'].next_by_code('puskesmas.pendaftaran.sequence') or _('New')
     #   result = super(puskesmas_pendaftaran, self).create(vals)
     #   return result