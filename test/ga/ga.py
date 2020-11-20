"""
@author lipo
@file test/ga/ga.py
@description ga单元测试

@createtime Fri, 20 Nov 2020 13:42:13 +0800
"""
from unittest import TestCase

from ga.ga import GA


class FakeSelector:
    ...


class FakePopulation:
    selector = None
    codec_plugin = None

    def use_selector(self, selector):
        self.selector = selector

    def iter_next(self, codec_plugin):
        self.codec_plugin = codec_plugin


class FakeIterPlugin:
    ga = None

    def __call__(self, ga):
        self.ga = ga


class FakeCodecPlugin:
    ...


class GaTestCase(TestCase):
    def setUp(self):
        self.fake_iter_plugin = FakeIterPlugin()
        self.fake_codec_plugin = FakeCodecPlugin()
        self.ga = GA(
            [self.fake_codec_plugin],
            [], [self.fake_iter_plugin], "")

    def testSetup(self):
        fake_population = FakePopulation()
        fake_selector = FakeSelector()
        self.ga.setup_population(fake_population)
        self.ga.use_selector(fake_selector)

        self.assertEqual(self.ga.population, fake_population)
        self.assertEqual(fake_population.selector, fake_selector)

        # run next
        self.ga.next()
        self.assertEqual(self.fake_iter_plugin.ga, self.ga)
        self.assertEqual(
            fake_population.codec_plugin, [self.fake_codec_plugin])
