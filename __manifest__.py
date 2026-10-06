# -*- coding: utf-8 -*-
# vim: tabstop=4 softtabstop=0 shiftwidth=4 smarttab expandtab fileformat=unix
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
{
    'name': "Signup Salesperson by Language",
    'summary': "New website customers get a salesperson chosen by the language they registered in",
    'description': """
Signup Salesperson by Language
==============================

On a multilingual website the right salesperson often depends on the
customer's language: the German-speaking team handles the German site, the
French-speaking team the French one.

This app adds a "Registration Salesperson" to every language (Settings >
Translations > Languages). When a customer signs up on the website, their
contact gets the Registration Salesperson of the language of the page they
registered on. If that language has none, the Salesperson set on the website
(eCommerce settings) is used.

It happens once, at signup. A salesperson changed later by your staff is
never overwritten.
""",
    'version': "18.0.1.0.2",
    'author': "Hadron for Business sp. z o.o.",
    'website': "http://hadronforbusiness.com",
    'license': "OPL-1",
    'category': "Website/Website",
    'depends': [
        'auth_signup',
        'website',
    ],
    'data': [
        'views/res_lang_views.xml',
    ],
    'images': [
        'static/description/banner_screenshot.png',
    ],
    'installable': True,
    'application': False,
}
