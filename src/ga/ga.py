from ga.lib.iterable import Iterable
from ga.plugins.plugins import CodecPlugin


class GA(Iterable):
    """
    指定GA流程

    一般GA整体上看去分为几个主要的流程
    """
    def __init__(
        self,
        codec_plugin: Union[str, List[str]],
        cm_plugin: Union[str, List[str]],
        iter_plugin: Union[str, List[str]],
        param_plugin: str
    ):
        pass

    def mutate(self):
        """变异"""
        pass

    def cross(self):
        """交叉"""
        pass

    def select(self):
        """选择"""
        pass

    def next(self):
        """
        指定步进算法流程
        """
        return False
