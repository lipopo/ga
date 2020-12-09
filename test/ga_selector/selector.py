from unittest import TestCase

from ga_selector.selector import Selector


class FakeIndividual:
    duplicated = False

    def duplicate(self):
        self.duplicated = True
        return self


class SelectorTestCase(TestCase):

    def calc_fitness(self, individual):
        return 1

    def setUp(self):
        self.selector = Selector(self.calc_fitness)

    def testSelector(self):
        self.assertEqual(self.selector.get_fitness, self.calc_fitness)

        individuals = [FakeIndividual()]
        self.assertFalse(individuals[0].duplicated)
        new_individuals = self.selector.select(individuals)
        self.assertTrue(new_individuals[0].duplicated)
