from odoo import api, fields, models
from odoo.exceptions import UserError, AccessError

tipo_chip = [
    ('1', 'Hondutel'),
    ('2', 'Tigo'),
    ('3', 'Claro'),
    ('4', 'Otros'),
]

info_chip = [
    ('ICC ', 'ICC'),
    ('PIN', 'PIN'),
    ('PUK', 'PUK'),
]


class salesaba_inherint_usuarios_aba(models.Model):
    _name = "creacion_usuarios_aba"
    
    name_agente_atlantida = fields.Char("Nombre de agente atlantida")
    codigo = fields.Integer("Codigo Completo")
    terminal = fields.Integer("Terminal")
    street = fields.Char('Direccion')
    street2 = fields.Char('Segunda direccion')

    #codigo_zip = fields.Char('Codigo Postal', change_default=True)
    city = fields.Char('Ciudad')
    state_id = fields.Many2one("res.country.state", string='Departamento')
    country_id = fields.Many2one('res.country', string='País')

    name_contacto = fields.Char("Nombre de contacto")
    phone = fields.Char('Telefono', track_visibility='onchange', track_sequence=5)
    rtn = fields.Char("RTN")
    tipo_chip_selec = fields.Selection(tipo_chip, string='Tipo Chip', index=True, default=tipo_chip[0][0])
    info_chip_selec = fields.Selection(info_chip, string='Informacion del chip', index=True, default=info_chip[0][0])    

    usuario = fields.Char("Usuarios")
    recibe_gestion = fields.Char("Recibe gestion")
    comentarios = fields.Text("Comentarios adicionales")
    token = fields.Integer("Token")
    tipo_terminal = fields.Integer("Tipo Terminal")
    usuarios_aba_id = fields.Many2one('sale.order',string="Usuarios Creacion")
    numer_sysaid = fields.Char("# SYSAID")

    

