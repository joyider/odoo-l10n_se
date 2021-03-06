# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
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
    'name': 'Account export XML',
    'version': '0.3',
    'category': 'account',
    'summary': 'Exports components from Accouting to XML',
    'description': """
Exports from accouting or other models to XML

For example:
* Customers
* Invoices
* Moves

Choose what model you want to export. Depth gives you how many levels of 
related models you want to export, it just gives you a list of models and
you can still choose what models you want. If your main model has periods
connected you can choose what periods you want to export data from.



""",
    'author': 'Vertel AB',
    'license': 'AGPL-3',
    'website': 'http://www.vertel.se',
    'depends': ['account',],
    'data': [ 'account_export_xml.xml',
    ],
    'application': False,
    'installable': True,
    'auto_install': False,
    
}
# vim:expandtab:smartindent:tabstop=4s:softtabstop=4:shiftwidth=4:
