from random import sample
from unittest import TestCase

from ga_cm.cm_plugin import CmPlugin


class FakeGenotype:
    code = []

    def __init__(self, code):
        self.code = code


class FakeIndividual:
    genotype = None
    phenotype = "Phenotype"

    def __init__(self, code):
        self.genotype = FakeGenotype(code)


class CmPluginTestCase(TestCase):

    def setUp(self):
        self.cm_plugin = CmPlugin(
            0.1, 0.1
        )
        self.code_base = [True] * 100 + [False] * 100

    def testCross(self):
        i1code = sample(self.code_base, 100)
        i2code = sample(self.code_base, 100)
        i1 = FakeIndividual(i1code)
        i2 = FakeIndividual(i2code)

        i1code_feature = sum(i1code)
        i2code_feature = sum(i2code)
        code_feature = i1code_feature + i2code_feature

        self.assertEqual(i1.genotype.code, i1code)
        self.assertEqual(i2.genotype.code, i2code)

        self.cm_plugin.cross(i1, i2)

        i1code_feature_now = sum(i1code)
        i2code_feature_now = sum(i2code)
        code_feature_now = i1code_feature_now + i2code_feature_now

        self.assertEqual(code_feature, code_feature_now)
        self.assertNotEqual(i1code_feature, i1code_feature_now)
        self.assertNotEqual(i2code_feature, i2code_feature_now)
        self.assertIsNone(i1.phenotype)
        self.assertIsNone(i2.phenotype)

    def testCrossover(self):
        self.assertEqual(self.cm_plugin.crossover_rate, 0.1)
        codes = []
        code_features = []
        individuals = []
        for _ in range(100):
            code = sample(self.code_base, 100)
            codes.append(code)
            code_features.append(sum(code))
            individuals.append(FakeIndividual(code))

        self.cm_plugin.crossover(individuals)

        code_features_now = []
        for code in codes:
            code_features_now.append(sum(code))

        self.assertNotEqual(code_features, code_features_now)
        self.assertEqual(sum(code_features), sum(code_features_now))

    def testMutate(self):
        self.assertEqual(self.cm_plugin.mutate_rate, 0.1)

        individual_code = sample(self.code_base, 100)
        individual = FakeIndividual(individual_code)
        code_feature = sum(individual_code)

        self.cm_plugin.mutate(individual)
        code_feature_now = sum(individual_code)

        self.assertNotEqual(code_feature, code_feature_now)