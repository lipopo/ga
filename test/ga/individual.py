from unittest import TestCase

from ga.individual import Individual


class FakeCodecPlugin:
    fake_gen = None
    fake_phe = None

    def __init__(self, genotype, phenotype):
        self.fake_gen = genotype
        self.fake_phe = phenotype

    def encode(self, phenotype):
        return self.fake_gen

    def decode(self, genotype):
        return self.fake_phe


class IndividualTestCase(TestCase):

    def setUp(self):
        self.individual = Individual()


    def testEncodeAndDecode(self):
        fake_codec_plugin = FakeCodecPlugin(1, 2)
        self.individual.use([fake_codec_plugin])

        self.assertEqual(
            self.individual.genotype, 1)

        self.assertEqual(
            self.individual.phenotype, 2)
