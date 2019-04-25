import json
import numpy as np
from . import parse

def descriptors(materials, embedding_file, operations=["wmean","wstd"]):
    """
    he
    """
    featuriser = Featuriser(embedding_file)
    statistics = Statistics(operations)

    descriptors_list = []
    for material in materials:
        elements, weights = parse.parse_composition(material)
        print(elements, weights)
        atom_features = atom_descriptors(elements, featuriser)
        material_features = material_descriptors(atom_features, weights, statistics)
        descriptors_list.append(material_features)

    features = np.vstack(descriptors_list)

    return features

def atom_descriptors(elements, featuriser):
    """
    he
    """
    atom_fea = np.vstack([featuriser.get_fea(element) for element in elements])
    return atom_fea

def material_descriptors(features, weights, statistics):
    """
    he
    """
    material_fea = statistics.dispatch(features, weights)
    return  material_fea

class Statistics(object):
    """
    Statistics object
    """
    def __init__(self, operations):
        self.operations = operations

    def dispatch(self, features, weights):
        data_list = []
        for operation in self.operations:
            method_name = "eval_" + str(operation)
            method = getattr(self, method_name)
            stat = method(features, weights)
            data_list.append(stat)
        data = np.hstack(data_list)
        return data

    def eval_wmean(self, features, weights):
        return np.average(features, axis=0, weights=weights)

    def eval_wstd(self, features, weights):
        wmean = self.eval_wmean(features, weights)
        return np.sqrt(np.average((features - wmean) ** 2, axis=0, weights=weights))

    def eval_geometric(self, features, weights):
        return np.exp(np.sum(weights*np.log(features), axis=0)/np.sum(weights, axis=0))

    def eval_harmonic(self, features, weights):
        return np.sum(weights, axis=0)/np.sum(weights/features, axis=0)

    def eval_max(self, features, weights):
        return np.max(features, axis=0)

    def eval_min(self, features, weights):
        return np.min(features, axis=0)

    def eval_range(self, features, weights):
        return np.ptp(features, axis=0)


class Featuriser(object):
    """
    Lookup dict object
    """
    def __init__(self, embedding_file):
        with open(embedding_file) as f:
            self.embedding = json.load(f)
        self.allowed_types = set(self.embedding.keys())

    def get_fea(self, key):
        assert key in self.allowed_types, "{} wasn't allowed".format(key)
        return self.embedding[key]

    def get_dict(self):
        return self.embedding

def load_file(file):
    """
    load file and return a list, files should contain one item per line

    example:    LaCu04
                K2MgO4
                NaCl
    """
    with open(file) as f:
        compositions = f.read().splitlines()
    return compositions
