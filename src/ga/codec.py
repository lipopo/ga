"""
@author lipo
@file ga/codec.py
@description 编解码器

@createtime Wed, 14 Oct 2020 15:20:26 +0800
"""
from ga.genotype import Genotype
from ga.phenotype import Phenotype


class Codec:

    def encode(self, phonetype: Phenotype) -> Genotype:
        """
        @name encode
        @description 编码流程

        @parameter phenotype 表现型

        @return Genotype 返回编码后的基因型对象
        """

    def decode(self, genotype: Genotype) -> Phenotype:
        """
        @name decode
        @description 解码流程

        @parameter genotype 基因型

        @return Phenotype 返回表现型对象
        """
