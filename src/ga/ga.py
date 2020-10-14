"""
@author lipo
@file ga/ga.py
@description 基础的GA对象

@createtime Wed, 14 Oct 2020 15:35:22 +0800
"""
from ga.codec import Codec
from ga.lib import Iterable
from ga.plugins import CodcPlugin, CmPlugin, \
    IterPlugin, GeneratePlugin


class GA(Iterable):
    def __init__(
        self,
        codec_plugin: Union[CodecPlugin, List[CodecPlugin]],
        cm_plugin: CmPlugin,
        iter_plugin: Union[IterPlugin, List[IterPlugin]],
        param_plugin: str,
        generate_plugin: Union[None, GeneratePlugin] = None
    ):
        self.iter_plugin = iter_plugin
        self.generate_plugin = generate_plugin

    def __call__(
        self,
        population: Population = None
    ):
        """
        @description 配置基础参数

        @parameter population 已知种群
        """
        if population is None and self.generate_plugin is not None:
            # 基于种群生成器，生成种群
            population = self.generate_plugin.generate()
        self.population = population

    def next(self):
        """
        @name next
        @description 指定步进算法流程
        """
        # 告知种群机进行下一次迭代
        self.population.iter()

        # 使用迭代控制器构建迭代切面
        for _iter in self.iter_plugin:
            _iter(self)
