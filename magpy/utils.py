from pkg_resources import resource_filename, resource_exists
import pandas as pd

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

def construct_dict(feature):
    """
    construct dictionary from reference tables
    """
    with open(resource_filename("magpy", "tables/" + feature + ".dat")) as f:
        d = dict(x.rstrip().split(None, 1) for x in f)

    return d

def combine_dfs(df_list):
    """
    combine a list of individual dataframes
    """
    return pd.concat(df_list, keys=(x for x in range(len(df_list))))