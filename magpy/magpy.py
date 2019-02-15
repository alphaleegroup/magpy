# MIT License

# Copyright (c) 2018, Rhys Goodall

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import re
import os.path
import pandas as pd
import numpy as np
from pkg_resources import resource_filename, resource_exists

"""
allowed features =  AtomicVolume,       AtomicWeight,           BoilingT,               
                    BoilingTemp,        BulkModulus,            Column,             
                    CovalentRadius,     Density,                ElectronAffinity,
                    Electronegativity,  FirstIonizationEnergy,  FusionEnthalpy,
                    GSbandgap,          GSenergy_pa,            GSestBCClatcnt,         
                    GSestFCClatcnt,     GSmagmom,               GSvolume_pa,        
                    HHIp,               HHIr,                   HeatCapacityMass,   
                    HeatCapacityMolar,  HeatFusion,             ICSDVolume,
                    IsAlkali,           IsDBlock,               IsFBlock,
                    IsMetal,            IsMetalloid,            IsNonmetal,         
                    MeltingT,           MendeleevNumber,        MiracleRadius,      
                    NUnfilled,          NValance,               NdUnfilled,
                    NdValence,          NfUnfilled,             NfValence,              
                    NpUnfilled,         NpValence,              NsUnfilled,         
                    NsValence,          Number,                 Polarizability,     
                    Row,                ShearModulus,           SpaceGroupNumber,
                    Wigner,             ZungerPP-r_d,           ZungerPP-r_p,           
                    ZungerPP-r_pi,      ZungerPP-r_s,           ZungerPP-r_sigma
"""

basic = [
    "CovalentRadius",
    "Polarizability",
    "Electronegativity",
    "ElectronAffinity",
    "FirstIonizationEnergy",
]

allowed_ops = ["wmean", "wstd", "wskew", "wkurtosis", "max", "min", "range"]


class FeatureError(Exception):
    pass


class OperationError(Exception):
    pass


def load_file(file):
    """
    load file and return a list, files should contain one item per line

    example:    LaCu04
                K2MgO4
                NaCl

    or:         CovalentRadius
                Polarizability
                Electronegativity
    """
    with open(file) as f:
        compositions = f.read().splitlines()
    return compositions


def save_file(df, output="output.csv"):
    df.to_csv(
        output,
        header=True,
        index=True,
        index_label=["CompositionIndex", "ElementIndex"],
    )


def parse_input(file):
    """
    take an input composition string and return an array of elements
    and an array of stoichometric coefficients.

    example: La2Cu04 -> (La Cu O) and (2 1 4)

    this is done in two stages, first formatting to ensure weights
    are explicate then parsing into sections:

    example: BaCu3 -> Ba1Cu3

    example: Ba1Cu3 -> (Ba Cu) & (1 3)

    """
    regex = r"([A-Z][a-z](?![0-9]))"
    regex2 = r"([A-Z](?![0-9]|[a-z]))"
    subst = r"\g<1>1"
    for i in range(len(file)):
        file[i] = re.sub(regex, subst, file[i].rstrip())
        file[i] = re.sub(regex2, subst, file[i])

    elements = np.empty_like(file, dtype=object)
    weights = np.empty_like(file, dtype=object)
    regex3 = r"(\d+\.\d+)|(\d+)"
    for i in range(len(file)):
        parsed = [j for j in re.split(regex3, file[i]) if j]
        elements[i] = parsed[0::2]
        weights[i] = parsed[1::2]
    return elements, weights


def construct_dict(feature):
    """
    construct dictionary from reference tables
    """
    with open(resource_filename("magpy", "tables/" + feature + ".dat")) as f:
        d = dict(x.rstrip().split(None, 1) for x in f)

    return d


def look_up(elements, weights, features=[""]):
    """
    build a dataframe containing the elementwise results for desired features

    """
    # ensure valid feature list

    if not features:
        raise FeatureError("No Features Given, specify 'features' kwarg")
    elif features == [""]:
        raise FeatureError("No Features Given, specify 'features' kwarg")
    else:
        not_valid = []
        for i in range(len(features)):
            if resource_exists("magpy", "tables/" + features[i] + ".dat"):
                pass
            else:
                not_valid.append(features[i])
        if not_valid:
            message = (
                "Specified Features (" + ", ".join(not_valid) +
                ") are not supported"
            )
            raise FeatureError(message)
        pass

    # lookup features for the different compositions
    df_list = []
    for i in range(len(elements)):
        df_list.append(collect_values(elements[i], weights[i], features))

    return df_list


def combine_dfs(df_list):
    """
    combine a list of individual dataframes
    """
    return pd.concat(df_list, keys=(x for x in range(len(df_list))))


def collect_values(elements, weights, features):
    """
    collect values from dictionaries
    """
    output = np.column_stack((elements, weights))
    for feature in features:
        d = construct_dict(feature)
        values = np.vectorize(d.get)(elements)
        output = np.column_stack((output, values))
    df = pd.DataFrame(output, columns=["Element", "Weights"] + features)

    return df


def get_descriptors(df_list, features, descriptors):
    """
    generate common statistics to represent each composition in list

    features array of str
    descriptors array of str
    """
    stat_list = []
    for i in range(len(df_list)):
        try:
            values = df_list[i][features].values.astype(float)
        except ValueError:
            print(i)
            print(df_list[i][features].values)
            raise(ValueError)
        weights = df_list[i]["Weights"].values.astype(float)

        chosen, data = eval_descriptors(values, weights, descriptors)
        output = np.column_stack((chosen, data))
        df = pd.DataFrame(output, columns=["Statistics"] + features)
        stat_list.append(df)

    return stat_list


def eval_descriptors(values, weights, descriptors):
    """
    """
    diff = np.setdiff1d(descriptors, allowed_ops)
    if diff:
        message = (
            "Specified Features ({}) are not supported".format(diff)
        )
        raise OperationError(message)

    chosen = np.intersect1d(descriptors, allowed_ops)
    generate = FeatureStatistics()
    generate.values = values
    generate.weights = weights
    data = generate.dispatch(chosen)

    return chosen, data


class FeatureStatistics:
    def __init__(self):
        self.values = np.empty(0)
        self.weights = np.empty(0)

    def dispatch(self, operations):
        data = np.empty((0, self.values.shape[1]))
        for operation in operations:
            method_name = "eval_" + str(operation)
            method = getattr(self, method_name)
            data = np.vstack((data, method()))
        return data

    def eval_wmean(self):
        return np.average(self.values, axis=0, weights=self.weights)

    def eval_wstd(self):
        '''
        note as we have exact composition strings we do not reduce the ddof 
        by 1 as we have the entire population.
        '''
        wmean = self.eval_wmean()
        return np.sqrt(np.average((self.values - wmean) ** 2,
                                  axis=0, weights=self.weights))

    def eval_geometric(self):
        return np.exp(np.sum(self.weights*np.log(self.values), axis=0)/np.sum(self.weights, axis=0))

    def eval_harmonic(self):
        return np.sum(self.weights, axis=0)/np.sum(self.weights/self.values, axis=0)

    def eval_max(self):
        return np.max(self.values, axis=0)

    def eval_min(self):
        return np.min(self.values, axis=0)

    def eval_range(self):
        return np.ptp(self.values, axis=0)
