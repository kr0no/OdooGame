# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

class player(models.Model):
    _name = 'ogame.player'
    _description = 'Players'

    name = fields.Char()
    planets = fields.One2many('ogame.planet', 'player')
    points = fields.Float(default=0)

class buildingType(models.Model):
    _name = 'ogame.buildingtype'
    _description = 'Building Types'

    name = fields.Char()
    cost_metal = fields.Float(default=0)
    cost_crystal = fields.Float(default=0)
    cost_duty = fields.Float(default=0)
    cost_multiplier = fields.Float(default=1.5)

class building(models.Model):
    _name = 'ogame.building'
    _description = 'Buildings'

    level = fields.Integer(default=0)
    building_type = fields.Many2one('ogame.buildingtype')
    planet = fields.Many2one('ogame.planet')

class planet(models.Model):
    _name = 'ogame.planet'
    _description = 'Planets'

    def _generate_fields(self):
        return random.randint(120, 150)

    name = fields.Char(default='Planeta principal')
    player = fields.Many2one('ogame.player')
    planet_fields = fields.Integer(default=_generate_fields)
    metal = fields.Float(default=500.0)
    crystal = fields.Float(default=500.0)
    duty = fields.Float(default=0.0)
    buildings = fields.One2many('ogame.building', 'planet')