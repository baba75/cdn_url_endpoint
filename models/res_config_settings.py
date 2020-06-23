from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cdn_endpoint = fields.Char(
        'CDN Endpoint',
        related='website_id.cdn_endpoint',
        readonly=False)