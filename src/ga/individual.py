"""
@author lipo
@file ga/invdividual.py
@description |
考虑到动态变异和动态交叉的流程，可以实现交叉率
和变异率的动态浮动，使得交叉变异过程能够在整个
系统演进过程中不断自行优化和退化

@createtime Mon, 12 Oct 2020 15:35:28 +0800
"""
from ga.genotype import Genotype
from ga.phenotype import Phenotype


class Individual:
    """
    抽象的个体

    fitness 计算环境适应度的数值
    """
    codec_plugin = None

    @property
    def fitness(self):
        """
        @name fitness
        @description 计算表现型的适应度，并返回适应度

        @return number 适应度数值
        """
        return 0

    @property
    def genotype(self) -> Genotype:
        """
        @name genotype
        @description 编码计算，并返回基因型对象

        @return Genotype 基因型
        """

    @property
    def phenotype(self) -> Phenotype:
        """
        @name phenotype
        @description 解码计算，并返回表现型对象

        @return Phenotype 表现型对象
        """

    def use(self, codec_plugin):
        self.codec_plugin = codec_plugin
