"""
@file test/ga_generate/generate_plugin.py
@author lipo
@description 生成器插件单元测试

@createtime
"""
from unittest import TestCase

from ga_generate.generate_plugin import GeneratePlugin


class FakeMeta:
    range_list = [(20, 23), (1, 20)]


class GeneratePluginTestCase(TestCase):

    def setUp(self):
        self.generate_plugin = GeneratePlugin(
            10, FakeMeta()
        )

    def testGenerate(self):
        population = self.generate_plugin.generate()
        self.assertEqual(len(population.individuals), 10)
