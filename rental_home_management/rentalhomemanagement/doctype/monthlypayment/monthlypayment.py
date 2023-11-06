# Copyright (c) 2023, Sowmiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class MonthlyPayment(Document):
        
    def validate(self):
        self.calculate_over_due()
        self.calculate_amount_to_be_paid()
        self.calculate_blnc_amount()
                
    def calculate_over_due(self):
        if self.monthly_rent and self.amount_paid:
            over_due = int(self.monthly_rent) - self.amount_paid
            self.over_due = over_due
        else:
            self.over_due = 0


    def calculate_blnc_amount(self):
        if self.monthly_rent and self.amount_paid:
            blnc_amount = float(self.monthly_rent) - self.amount_paid
            if blnc_amount >= 1000:
                    self.blnc_amount = blnc_amount
                    self.fine_amount = 500
            else:
                self.blnc_amount = blnc_amount
                self.fine_amount = 0
        else:
            self.blnc_amount = 0
            self.fine_amount = 0

    def calculate_amount_to_be_paid(self):
        if self.blnc_amount and self.fine_amount :
            amount_to_be_paid = self.blnc_amount + self.fine_amount 
            self.amount_to_be_paid = amount_to_be_paid
        else:
            self.amount_to_be_paid = 0