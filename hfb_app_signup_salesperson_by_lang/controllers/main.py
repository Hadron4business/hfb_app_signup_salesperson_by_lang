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
"""	@version	18.0.1.0.2
	@owner  Hadron for Business
	@author Hadron for Business sp. z o.o.
	@date   2026.10.06

	Assign salesperson at signup
	Extends the website signup: right after the account is created, the contact
	receives the Registration Salesperson of the page language, or the website's
	own salesperson as a fallback.
"""
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.http import request


class SignupSalespersonHome(AuthSignupHome):

    def do_signup(self, qcontext, *args, **kwargs):
        result = super().do_signup(qcontext, *args, **kwargs)

        login = qcontext.get('login')
        if login:
            user = request.env['res.users'].sudo().search(
                [('login', '=', login)], limit=1)
            if user.partner_id:
                self._assign_salesperson_by_signup_lang(user.partner_id)

        return result

    def _assign_salesperson_by_signup_lang(self, partner):
        """Salesperson for a brand-new customer: the Registration Salesperson
        of the language they registered in, falling back to the Salesperson
        of the current website (when the eCommerce app is installed). Runs once, at signup, so a Salesperson set
        later by staff is never overwritten."""
        lang_code = request.lang.code if request.lang else False
        salesperson = request.env['res.lang'].sudo().search(
            [('code', '=', lang_code)], limit=1).registration_salesperson_id

        if not salesperson and getattr(request, 'website', False):
            # The website Salesperson only exists when website_sale is installed.
            salesperson = getattr(request.website, 'salesperson_id', False)

        if salesperson:
            partner.sudo().write({'user_id': salesperson.id})

#EoF
