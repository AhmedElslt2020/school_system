from datetime import date
from odoo import models, fields, api, tools, _
from odoo.exceptions import ValidationError


class YearYear(models.Model):
    _name = "year.year"
    _rec_name = "year"



    year = fields.Integer()
    number_of_class = fields.Integer(string="number of class")


