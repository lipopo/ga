from unittest import TestCase

from ga.population import Population


class FakeCmPlugin:
    m_count = 0
    c_count = 0

    def mutate(self, individual):
        self.m_count += 1

    def crossover(self, individuals):
        self.c_count = len(individuals)


class FakeSelector:
    i_count = 0

    def select(self, individuals):
        self.i_count = len(individuals)
        return individuals


class PopulationTestCase(TestCase):

    def setUp(self):
        self.population = Population()

    def testMutateCross(self):
        fake_cm_plugin = FakeCmPlugin()
        self.population.individuals = [1, 2, 3]
        self.population(fake_cm_plugin)
        self.population.mutate()
        self.population.cross()

        self.assertEqual(self.population.cm_plugin, fake_cm_plugin)
        self.assertEqual(
            fake_cm_plugin.c_count, fake_cm_plugin.m_count)

    def testSelect(self):
        fake_selector = FakeSelector()
        self.population.use_selector(fake_selector)
        self.population.individuals = [1, 2, 3]
        self.population.select()

        self.assertEqual(
            fake_selector.i_count, len(self.population.individuals))
