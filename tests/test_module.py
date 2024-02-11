# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.tests.test_tryton import ModuleTestCase


class AccountInvoicePriceListTestCase(ModuleTestCase):
    "Test Account Invoice Price List module"
    module = 'account_invoice_price_list'


del ModuleTestCase
