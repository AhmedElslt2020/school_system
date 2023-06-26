from datetime import date
from odoo import models, fields, api, tools, _
from odoo.exceptions import ValidationError


class StudentStudent(models.Model):
    _name = "student.student"


    name = fields.Char(string="Name")
    class_id = fields.Many2one("class.class")
    class_year = fields.Many2one(related="class_id.year_id")
    subject_ids = fields.One2many("subject.subject","student_id")



