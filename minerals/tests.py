from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Mineral


class MineralViewTest(TestCase):
    def setUp(self):
        too_many = "a" * 1000
        self.min = Mineral.objects.create(
            name="mineral A",
            image_filename="minerala.jpeg"
        )
        self.min2 = Mineral.objects.create(
            name="mineral B",
            image_filename="mineralB.jpeg"
        )
        self.min3 = Mineral.objects.create(
            name="mineral C",
            color="red"
        )
        self.rock = Mineral.objects.create(
            name='pet rock',
            image_filename='rock.jpb',
            image_caption=52,
            category=too_many
        )

    def test_mineral_model(self):
        self.assertRaises(ValueError)
        self.assertTrue(self.rock.name == 'pet rock')
        self.assertTrue(type(self.rock.name), "<class 'str'>")

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.min, resp.context['minerals'])
        self.assertIn(self.min2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/home.html')
        self.assertContains(resp, self.min.name)
        self.assertContains(resp, self.min3.name)
        self.assertContains(resp, self.min3.color)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk':1}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.min.name)
