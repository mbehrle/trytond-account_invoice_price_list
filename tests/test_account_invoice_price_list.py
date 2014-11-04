#!/usr/bin/env python
# This file is part account_invoice_price_list module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends


class AccountInvoicePriceListTestCase(unittest.TestCase):
    'Test Account Invoice Price List module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('account_invoice_price_list')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        AccountInvoicePriceListTestCase))
    return suite
