# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    "name": "Payment term next days2 instance",
    "version": "1.0",
    "author": "bisnesmart",
    "category": "Accounting",
    "website": "http://www.bisnesmart.com",
    'description' : """
    Payment term next days2 fix.
    ----------------------------
    When computing a value for a payment day, the next instance of the value
    in the field days2 is the one selected, instead of the one of the month after.

    Example:
    --------

    days = 30
    days2 = 3
    Current date : 03-01-2016

    30 days after, it will be 02-02-2016. With the default odoo behaviour,
    the day computed for the payment would be 03-03-2016, but with this module
    it will be 03-02-2016.

    """,
    "depends": [
        "account",
    ],
    "data": [
    ],
    'installable': True
}
