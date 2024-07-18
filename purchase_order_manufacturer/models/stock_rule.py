# Copyright (C) 2024 Akretion (<http://www.akretion.com>).
# @author Mathieu Delva <mathieu.delva@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class StockRule(models.Model):
    _inherit = "stock.rule"

    def _make_po_get_domain(self, company_id, values, partner):
        """ """
        domain = super(StockRule, self)._make_po_get_domain(company_id, values, partner)
        domain += (
            (
                "manufacturer_id",
                "=",
                values["move_dest_ids"].product_id.manufacturer_id.id,
            ),
        )
        return domain
