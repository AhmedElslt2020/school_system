from datetime import date
from odoo import models, fields, api, tools, _
from odoo.exceptions import ValidationError


class SubjectSubject(models.Model):
    _name = "subject.subject"


    name = fields.Char(string="Name")
    year_id = fields.Many2one("year.year")
    student_id = fields.Many2one("student.student")



