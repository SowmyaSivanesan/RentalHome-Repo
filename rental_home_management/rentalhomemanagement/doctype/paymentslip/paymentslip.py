# Copyright (c) 2023, Sowmiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PaymentSlip(Document):

    def validate(self):
        self.calculate_blnc_amount()

    def calculate_blnc_amount(self):
        if self.monthly_rent and self.amount_paid:
            blnc_amount = float(self.monthly_rent) - self.amount_paid
            if blnc_amount > 1000:
                    self.blnc_amount = blnc_amount
                    self.fine_amount = 500
            else:
                self.blnc_amount = blnc_amount
                self.fine_amount = 0
        else:
            self.blnc_amount = 0
            self.fine_amount = 0
