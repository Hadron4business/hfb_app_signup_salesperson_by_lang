# -*- coding: utf-8 -*-
#################################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2017-2026 Hadron for Business sp. z o.o. (http://hadronforbusiness.com)
#
# This program is proprietary software, licensed under the Odoo Proprietary
# License v1.0 (OPL-1). Its use is governed by the Odoo Apps terms available
# at https://www.odoo.com/documentation/user/legal/licenses.html and the
# license agreement accepted at purchase / installation.
#
# It is forbidden to publish, distribute, sublicense, or sell copies of the
# Software or modified copies of the Software.
#
# The above copyright notice and this permission notice must be included in
# all copies or substantial portions of the Software.
#
#################################################################################
"""	@version	19.0.1.0.0
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.06

	Registration salesperson per language
	Adds the Registration Salesperson field to languages.
"""
from odoo import fields, models


class ResLang(models.Model):
    _inherit = 'res.lang'

    registration_salesperson_id = fields.Many2one(
        'res.users', string="Registration Salesperson",
        help="Assigned as Salesperson to a new customer who registers on a "
             "website page in this language. When empty, the Salesperson "
             "set on the website is used. Only applied at signup - never "
             "overwrites a Salesperson changed afterwards.",
    )

#EoF
