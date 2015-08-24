#This file is part account_invoice_price_list module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields
from trytond.transaction import Transaction

__all__ = ['InvoiceLine']
__metaclass__ = PoolMeta


class InvoiceLine:
    __name__ = 'account.invoice.line'

    @fields.depends('party', 'invoice')
    def on_change_product(self):
        Product = Pool().get('product.product')

        super(InvoiceLine, self).on_change_product()
        party = self.party or self.invoice.party

        if (party and party.sale_price_list and self.product
                and self.invoice.type in ['out_invoice', 'out_credit_note']):
            with Transaction().set_context({
                    'price_list': party.sale_price_list.id,
                    'customer': party.id,
                }):

                prices = Product.get_sale_price([self.product], self.quantity or 0)
                self.unit_price = prices[self.product.id]
