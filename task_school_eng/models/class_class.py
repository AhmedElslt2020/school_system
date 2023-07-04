from datetime import date
from odoo import models, fields, api, tools, _
from odoo.exceptions import ValidationError


class ClassClass(models.Model):
    _name = "class.class"


    name = fields.Char(string="Name")
    year_id = fields.Many2one("year.year")


