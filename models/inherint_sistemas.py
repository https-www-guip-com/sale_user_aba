from odoo import api, fields, models
import odoo.addons.decimal_precision as dp


class SaleOrderOperaciones(models.Model):
    _inherit = "crm_flujo_nuevo_operaciones"

    sale_id = fields.Many2one('sale.order', string="Mostrar info de la oportunidad",
                                  help="Desde este campo puedes ver el inicio de la oportunidad en el CRM" ,
                                  ondelete='cascade', index=True)

class SaleOrderPlataforma(models.Model):
    _inherit = "crm_flujo_nuevo_sistemas"

    sale_id = fields.Many2one('sale.order', string="Mostrar info de la oportunidad",
                                  help="Desde este campo puedes ver el inicio de la oportunidad en el CRM" ,
                                  ondelete='cascade', index=True)