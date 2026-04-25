from odoo import models, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_force_register_payment(self):
        if not self:
            raise UserError(_("No bills selected."))

        if any(move.state != 'posted' for move in self):
            raise UserError(_("You can only register payments for posted vendor bills."))

        if any(move.move_type == 'entry' for move in self):
            raise UserError(_("Miscellaneous entries cannot be paid."))

        return super().action_force_register_payment()