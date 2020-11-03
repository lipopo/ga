"""
@author lipo
@file ga/invdividual.py
@description |
考虑到动态变异和动态交叉的流程，可以实现交叉率
和变异率的动态浮动，使得交叉变异过程能够在整个
系统演进过程中不断自行优化和退化

@createtime Mon, 12 Oct 2020 15:35:28 +0800
"""
from typing import Union, List

from ga.plugins import CodecPlugin
from ga.genotype import Genotype
from ga.phenotype import Phenotype


class Individual:
    """
    抽象的个体

    fitness 计算环境适应度的数值
    """
    codec_plugin: Union[None, List[CodecPlugin]] = None
    _phenotype: Union[None, _phenotype] = None
    _genotype: Union[None, _genotype] = None

    @property
    def genotype(self) -> Genotype:
        """
        @name genotype
        @description 编码计算，并返回基因型对象

        @return Genotype 基因型
        """
        if self._genotype is not None:
            return self._genotype

        _genotype = None
        for cp in self.codec_plugin:
            _genotype = cp.encode(self._phenotype)

        self._genotype = _genotype
        return _genotype

    @genotype.setter
    def set_genotype(self, value: Genotype):
        self._genotype = Genotype

    @property
    def phenotype(self) -> Phenotype:
        """
        @name phenotype
        @description 解码计算，并返回表现型对象

        @return Phenotype 表现型对象
        """
        if self._phenotype is not None:
            return self._phenotype

        _phenotype = None
        for cp in self.codec_plugin[::-1]:
            _phenotype = cp.decode(self._genotype)

        self._phenotype = _phenotype
        return _phenotype

    @phenotype.setter
    def set_phenotype(self, value: Phenotype):
        self._phenotype = value

    def use(self, codec_plugin: List[CodecPlugin]):
        self.codec_plugin = codec_plugin

    def duplicate(self):
        """
        个体复制
        """
        instance = self.__class__()
        instance.codec_plugin = self.codec_plugin
        instance._phenotype = self._phenotype
        instance._genotype = self._geotype
        return instance
