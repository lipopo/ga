"""
@author lipo
@file ga/genetype.py
@description 基础基因型文件

@cratetime Wed, 14 Oct 2020 15:10:38 +0800
"""


class Genotype:
    _code = None

    def mutate(self):
        """
        @name mutate
        @description 变异
        """

    def cross(self, right):
        """
        @name cross
        @description 交叉

        @parameter right 隔壁基因型
        """
