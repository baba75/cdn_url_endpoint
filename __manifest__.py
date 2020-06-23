# -*- coding: utf-8 -*-
{
    'name': "Odoo CDN Url Endpoint",

    'summary': """
        Odoo Content Delivery Network endpoint""",

    'description': """
        The CDN option in Odoo join the base_url of the CDN and the path,
        e.g: https://mycdn.com/rest/of/url
        
        This module add the possibility to have an extended endpoint,
        for example https://mycdn.com/endpoint/rest/of/url
        
    """,

    'author': "Alberto Carollo",
    'website': "http://www.ecobeton.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '12.0',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}