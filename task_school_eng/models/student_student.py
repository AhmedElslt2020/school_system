from datetime import date
from odoo import models, fields, api, tools, _
from odoo.exceptions import ValidationError


class StudentStudent(models.Model):
    _name = "student.student"


    name = fields.Char(string="Name")
    class_id = fields.Many2one("class.class")
    class_year = fields.Many2one(related="class_id.year_id")
    subject_ids = fields.One2many("subject.subject","student_id")
    date_of_birth = fields.Date(string='Date of Birth')
    number_of_student = fields.Char(string='Number of Student')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    gender = fields.Selection(string="Gender", selection=[('male', 'Male'), ('female', 'Female')], default='male')

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    @api.constrains("age")
    def check_something(self):
        for record in self:
            if record.age < 7:
                raise ValidationError(_("the age is smaller than seven"))

    _sql_constraints = [
        ('unique_number_of_student',
         'UNIQUE(number_of_student)',
         "The number is not unique you must change it"),
    ]



