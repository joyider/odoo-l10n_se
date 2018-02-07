# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Enterprise Management Solution, third party addon
#    Copyright (C) 2017 Vertel AB (<http://vertel.se>).
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

from odoo import api, fields, models, _
import logging
_logger = logging.getLogger(__name__)


class account_financial_report(models.Model):
    _inherit = 'account.financial.report'

    tax_ids = fields.Many2many(comodel_name='account.tax', string='Account Tax')

    @api.model
    def create(self, vals):
        if 'tax_ids' in vals:
            vals['account_ids'] = [(6, _, self.env['account.tax'].browse(vals['tax_ids'][0][2]).mapped('account_id').mapped('id'))]
        return super(account_financial_report, self).create(vals)

    @api.multi
    def write(self, vals):
        if 'tax_ids' in vals:
            vals['account_ids'] = [(6, _, self.env['account.tax'].browse(vals['tax_ids'][0][2]).mapped('account_id').mapped('id'))]
        return super(account_financial_report, self).write(vals)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: