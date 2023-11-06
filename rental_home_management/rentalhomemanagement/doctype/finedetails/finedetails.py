# Copyright (c) 2023, Sowmiya and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FineDetails(Document):
	def validate(self):
		self.calculate_blnc_due()

	def calculate_blnc_due(self):
		if self.amount_to_be_paid and self.amount_paying:
			blnc_due = float(self.amount_to_be_paid) - self.amount_paying
			if blnc_due > 0:
				self.blnc_due = blnc_due
				self.fine_deatils = "Yes"
			    
			else:
				self.blnc_due = blnc_due
				self.fine_deatils = "No"
		else:
			self.blnc_due = 0