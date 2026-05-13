# Vendor Bill Payment Validation

![Odoo 19](https://img.shields.io/badge/Odoo-19.0-875A7B?style=flat-square)
![License](https://img.shields.io/badge/License-LGPL--3-blue?style=flat-square)
![Category](https://img.shields.io/badge/Category-Accounting-4ECDC4?style=flat-square)

Restrict payment registration so only valid vendor bills can enter the payment flow in Odoo 19.

This module adds a small but important safeguard around payment registration. It intercepts `action_force_register_payment()` on `account.move` to make sure users only register payments from posted vendor bills, while explicitly blocking miscellaneous journal entries.

## Highlights

- Allows payment registration only for **posted vendor bills**.
- Blocks miscellaneous journal entries from the payment flow.
- Raises clear user-facing errors when selection rules are violated.
- Keeps the standard Odoo payment registration flow once validation passes.

## Technical Notes

- `models/account_move.py`
  Extends `account.move.action_force_register_payment()` with lightweight validation before delegating to the native behavior.

## Module Layout

```text
vendor_bill_payment_validation/
|-- models/
`-- __manifest__.py
```

## Dependencies

- `account`

## Installation

1. Place the module in your custom addons path.
2. Update the Apps list in Odoo.
3. Install **Vendor Bill Payment Validation**.

## License

This module is licensed under `LGPL-3`.
