"""
@file test/ga_codec/codec_plugin.py
@author lipo
@description codec插件单元测试

@createtime
"""
from unittest import TestCase
from ga_codec.codec_plugin import CodecPlugin


class FakePhenotype:
    phenotype = []

    def __init__(self, phenotype):
        self.phenotype = phenotype


class FakeGenotype:
    code = []

    def __init__(self, code):
        self.code = code


class FakeMeta:
    range_list = []
    bit_count = []

    def __init__(self, range_list, bit_count):
        self.range_list = range_list
        self.bit_count = bit_count


class CodecPluginTestCase(TestCase):

    def setUp(self):
        self.codec_plugin = CodecPlugin()

    def testEncode(self):
        phenotype = FakePhenotype([23.6])
        meta = FakeMeta([(23, 24)], [4])
        code = self.codec_plugin.encode(phenotype, meta)
        self.assertEqual(code, [True, False, False, True])

    def testDecode(self):
        genotype = FakeGenotype([True, False, False, True])
        meta = FakeMeta([(23, 24)], [4])
        val = self.codec_plugin.decode(genotype, meta)
        self.assertEqual(val, [23.6])
