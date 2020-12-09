import math

from ga import GA, Individual, IndividualMeta, Selector
from ga_codec import CodecPlugin
from ga_cm import CmPlugin
from ga_iter import StopIterPlugin
from ga_generate import GeneratePlugin
from ga_selector import Selector


def get_fitness(individual: Individual):
    val = individual.phenotype.phenotype
    return -math.log(abs(val[0] - 19.1))


def run_simple_ga():
    individual_meta = IndividualMeta()
    individual_meta.range_list = [(19, 20)]
    individual_meta.bit_count = [100]

    codec_plugin = CodecPlugin()
    cm_plugin = CmPlugin(0.1, 0.1)
    stop_iter_plugin = StopIterPlugin(100)
    generate_plugin = GeneratePlugin(100, individual_meta)

    selector = Selector(get_fitness)

    ga = GA(
        codec_plugin,
        cm_plugin,
        stop_iter_plugin,
        "",
        generate_plugin
    )
    ga.setup_population()  # 初始化种群
    ga.use_selector(selector)

    for idx, _ in enumerate(ga):
        print(sum([i.phenotype.phenotype[0] for i in ga.population.individuals]) / len(ga.population.individuals))


if __name__ == "__main__":
    run_simple_ga()
