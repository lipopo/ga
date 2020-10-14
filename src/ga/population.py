"""
@author lipo
@file ga/population.py
@description 种群对象

@cratetime Wed, 14 Oct 2020 15:37:28 +0800
"""
from ga.selector import Selector


class Pupolation:
    """
    种群

    种群本质上是个体的集合
    主要是一个个体的集合
    """
    cm_plugin = None
    individuals = []

    def cross(self):
        """
        @name cross
        @description 种群内部交叉
        """
        self.individuals = self.cm_plugin.crossover(self.individuals)

    def mutate(self):
        """
        @name cross
        @description 种群内变异
        """
        for individual in self.individuals:
            self.cm_plugin.mutate(individual)

    def select(self):
        """
        @name select
        @description 进行选择
        """
        self.individuals = self.selector.select(self.inviduals)

    def bind(self):
        for individual in self.individuals:
            individual.use(codec_plugin)

    def iter(
        self,
        codec_plugin,
        cm_plugin,
        param_plugin
    ):
        """
        @name iter
        @description 种群迭代

        @parameter codec_plugin 编解码插件
        @parameter cm_plugin 交叉变异插件
        @parameter param_plugin 参数插件
        """
        # 编解码器优化
        if self.codec_plugin != codec_plugin:
            self.codec_plugin = codec_plugin
            self.bind()  # 重新绑定编解码器

        self.cross()  # 进行交叉
        self.mutate()  # 引发变异
        self.select()  # 进行选择
