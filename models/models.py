# -*- coding: utf-8 -*-

import re
from werkzeug import urls
from odoo import models, fields, api

class Website(models.Model):
    _inherit = "website"
    
    cdn_endpoint = fields.Char('CDN Endpoint', default='')
    
    def get_cdn_url(self, uri):
        self.ensure_one()
        if not uri:
            return ''
        cdn_url = self.cdn_url
        cdn_endpoint = self.cdn_endpoint
        cdn_filters = (self.cdn_filters or '').splitlines()
        for flt in cdn_filters:
            if flt and re.match(flt, uri):
                return urls.url_join(cdn_url, cdn_endpoint + uri)
        return uri
