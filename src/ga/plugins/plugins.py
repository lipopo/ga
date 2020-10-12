from ga.plugins.plugin_type import PluginType


class Plugin:
    plugin_name = ""
    plugin_type = PluginType.Undefined

    @classmethod
    def use(cls, name: str):
        # 选择需要的插件
        _ins = None
        for _subcls in cls.__subclasses__():
            if _subcls.plugin_name == name:
                _ins = _subcls()
                break
        return _ins


class CodecPlugin(Plugin):
    plugin_type = PluginType.Codec

    def encode(self):
        pass

    def decode(self):
        pass


class CmPlugin(Plugin):
    plugin_type = PluginType.Cm

    def mutate(self):
        pass

    def crossover(self):
        pass


class IterPlugin(Plugin):
    plugin_type = PluginType.Iter

    def iter_next(self):
        pass


class ParamPlugin(Plugin):
    plugin_type = PluginType.Param

    def param_input(self):
        pass

    def param_output(self):
        pass


class GeneratePlugin(Plugin):
    plugin_type = PluginType.Generate

    def generate(self):
        pass
