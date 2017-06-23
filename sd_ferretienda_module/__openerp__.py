# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Sistemas de Datos (<http://www.sdatos.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name' : 'SDatos Ferretienda',
    'version' : '1.3',
    'author' : 'Sistemas de Datos',
    'maintainer': 'Sistemas de Datos',
    'category' : 'Interface',
    'sequence': 10,                
    'summary': 'Custom reports for clients',
    'description' : """
Ferretienda Module
==================

Module that modifies the program interface and the reports to Ferretería la llave
---------------------------------------------------------------------------------
* EDIT Header
* EDIT Footer
* EDIT Report invoice 
* EDIT Repor sale order
    """,
    'website': 'http://www.sdatos.com',
    # End General Data
    'depends' : ['web',
                 'account',
                 'report',
                 'sale_stock',
                 'point_of_sale',
                 'product'],            
    'data': ['report/inherit_footer.xml',
             'report/inherit_header.xml',
             'report/inherit_saleorder.xml',
             'report/inherit_invoice.xml',
             'report/invoice_summary.xml',
             'views/inherit_product_view.xml',
             'views/inherit_search_pos.xml',
             'static/src/xml/sd_pos.xml'],
    'images':[], 
    'installable': True,        
    'auto_install': False,        
    'application': False,
}