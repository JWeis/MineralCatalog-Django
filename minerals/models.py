import json
from django.db import models

# Create your models here.


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=1000)
    image_caption = models.CharField(max_length=1000)
    category = models.CharField(max_length=1000)
    formula = models.CharField(max_length=1000)
    strunz_classification = models.CharField(max_length=1000)
    crystal_system = models.CharField(max_length=1000)
    unit_cell = models.CharField(max_length=1000)
    color = models.CharField(max_length=1000)
    crystal_symmetry = models.CharField(max_length=1000)
    cleavage = models.CharField(max_length=1000)
    mohs_scale_hardness = models.CharField(max_length=1000)
    luster = models.CharField(max_length=1000)
    streak = models.CharField(max_length=1000)
    diaphaneity = models.CharField(max_length=1000)
    optical_properties = models.CharField(max_length=1000)
    refractive_index = models.CharField(max_length=1000)
    crystal_habit = models.CharField(max_length=1000)
    specific_gravity = models.CharField(max_length=1000)
    group = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def data_import(cls):
        json_data = open('minerals/minerals.json')
        all_data = json.load(json_data)
        json_data.close()
        for data in all_data:
            try:
                name = data['name']
            except KeyError:
                name = ''
            try:
                image_filename = data['image filename']
            except KeyError:
                image_filename = ''
            try:
                image_caption = data['image caption']
            except KeyError:
                image_caption = ''
            try:
                category = data['category']
            except KeyError:
                category = ''
            try:
                formula = data['formula']
            except KeyError:
                formula = ''
            try:
                strunz_classification = data['strunz classification']
            except KeyError:
                strunz_classification = ''
            try:
                crystal_system = data['crystal system']
            except KeyError:
                crystal_system = ''
            try:
                unit_cell = data['unit cell']
            except KeyError:
                unit_cell = ''
            try:
                color = data['color']
            except KeyError:
                color = ''
            try:
                crystal_symmetry = data['crystal symmetry']
            except KeyError:
                crystal_symmetry = ''
            try:
                cleavage = data['cleavage']
            except KeyError:
                cleavage = ''
            try:
                mohs_scale_hardness = data['mohs scale hardness']
            except KeyError:
                mohs_scale_hardness = ''
            try:
                luster = data['luster']
            except KeyError:
                luster = ''
            try:
                streak = data['streak']
            except KeyError:
                streak = ''
            try:
                diaphaneity = data['diaphaneity']
            except KeyError:
                diaphaneity = ''
            try:
                optical_properties = data['optical properties']
            except KeyError:
                optical_properties = ''
            try:
                refractive_index = data['refractive index']
            except KeyError:
                refractive_index = ''
            try:
                crystal_habit = data['crystal habit']
            except KeyError:
                crystal_habit = ''
            try:
                specific_gravity = data['specific gravity']
            except KeyError:
                specific_gravity = ''
            try:
                group = data['group']
            except KeyError:
                group = ''
            Mineral(
                name = name,
                image_filename = image_filename,
                image_caption = image_caption,
                category = category,
                formula = formula,
                strunz_classification = strunz_classification,
                crystal_system = crystal_system,
                unit_cell = unit_cell,
                color = color,
                crystal_symmetry = crystal_symmetry,
                cleavage = cleavage,
                mohs_scale_hardness = mohs_scale_hardness,
                luster = luster,
                streak = streak,
                diaphaneity = diaphaneity,
                optical_properties = optical_properties,
                refractive_index = refractive_index,
                crystal_habit = crystal_habit,
                specific_gravity = specific_gravity,
                group = group
            ).save()
