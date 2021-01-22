import logging
from datetime import date
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, tools, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.tools import email_re, email_split
from odoo.exceptions import UserError, AccessError



class PurchaseABAOrderAba(models.Model):
    _inherit = "pruchase.order"

    crm_operaciones_id = fields.Many2one('crm_flujo_nuevo_operaciones', string="Mostrar Seguimiento Operaciones",
                                  help="Desde este campo puedes ver el seguimiento de la oportunidad desde el lado de la plataforma" ,
                                  ondelete='cascade', index=True)
                                  