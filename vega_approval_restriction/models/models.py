# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT as DTF
from odoo.exceptions import UserError, AccessError, ValidationError

class Holidays(models.Model):
	_inherit = 'hr.holidays'
	
	is_manager = fields.Boolean(string="Manager")
	current_user = fields.Many2one('res.users','Current User', default=lambda self: self.env.user)

	@api.onchange('employee_id')
	def onchange_employee(self):
		self.is_manager = self.employee_id.manager

	@api.multi
	def action_approve(self):
		if self.employee_id.user_id.id == self.env.uid and self.employee_id.manager == True:
			raise UserError(_('Unauthorize! Cannot approve your own leave'))
		return super(Holidays, self).action_approve()

	@api.multi
	def action_refuse(self):
		for record in self:
			record.number_of_days_temp = 0.0
		return super(Holidays, self).action_refuse()