"""
考虑到动态变异和动态交叉的流程，可以实现交叉率
和变异率的动态浮动，使得交叉变异过程能够在整个
系统演进过程中不断自行优化和退化

@createtime Mon, 12 Oct 2020 15:35:28 +0800
"""


class Individual:
    """
    抽象的个体

    fitness 计算环境适应度的数值
    """

    def __gt__(self, other):
        return self.fitness > other.fitness

    def mutate(self):
        """变异

        指定变异率对于指定
        个体进行变异
        """
        pass

    def cross(self, other):
        """交叉

        主要通过指定交叉率
        进行一定成都的交叉
        同时生成两个个体
        """
        pass

    @property
    def fitness(self):
        """适应度数值"""
        return 0

    def get_fitness(self):
        ...

    def encode(self):
        ...

    def decode(self):
        ...
