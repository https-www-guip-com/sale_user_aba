from odoo import api, fields, models
import odoo.addons.decimal_precision as dp

tipo_chip = [
    ('1', 'Claro'),
    ('2', 'Tigo'),
    ('3', 'Hondutel'),
    ('4', 'Otros'),
]

tipo_terminales = [
    ('1', 'Terminal 1'),
    ('2', 'Terminal 2'),
    ('3', 'Otros'),
]

class SaleOrderOperaciones(models.Model):
    _inherit = "crm_flujo_nuevo_operaciones"

    sale_id = fields.Many2one('sale.order', string="Mostrar info de la oportunidad",
                                  help="Desde este campo puedes ver el inicio de la oportunidad en el CRM" ,
                                  ondelete='cascade', index=True)

    name_agente_atlantida = fields.Char("Nombre de agente atlantida")
    codigo = fields.Integer("Codigo Completo")
    terminal = fields.Integer("Terminal")
    street = fields.Char('Direccion')
    street2 = fields.Char('Segunda direccion')

    #codigo_zip = fields.Char('Codigo Postal', change_default=True)
    #city = fields.Char('Ciudad')
    #state_id = fields.Many2one("res.country.state", string='Departamento')
    #country_id = fields.Many2one('res.country', string='País')
    #phone = fields.Char('Telefono', track_visibility='onchange', track_sequence=5)
    
    name_contacto = fields.Char("Nombre de contacto")
    rtn = fields.Char("RTN")
    tipo_chip_selec = fields.Selection(tipo_chip, string='Tipo Chip', index=True, default=tipo_chip[0][0])
    usuario = fields.Char("Usuarios")
    recibe_gestion = fields.Char("Recibe gestion")
    comentarios = fields.Text("Comentarios adicionales")
    token = fields.Integer("Token")
    tipo_terminal = fields.Selection(tipo_terminales, string='Tipo de terminal', index=True, default=tipo_terminales[0][0])
    usuarios_aba_id = fields.Many2one('sale.order',string="Usuarios Creacion")



class SaleOrderPlataforma(models.Model):
    _inherit = "crm_flujo_nuevo_sistemas"

    sale_id = fields.Many2one('sale.order', string="Mostrar info de la oportunidad",
                                  help="Desde este campo puedes ver el inicio de la oportunidad en el CRM" ,
                                  ondelete='cascade', index=True)