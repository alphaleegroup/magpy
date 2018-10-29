import sys
import re
import pandas as pd
import numpy as np
from lookup import look_up


def load_file(file):
    '''
    loads file and returns a list, files should contain one composition per line

    example:    LaCu04
                K2MgO4
                NaCl
    '''
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


def parse_input(file):
    '''
    takes an input of the form composition string and returns an array of elements and
    an array of stoichometric coefficients.

    example: La2Cu04 -> (La Cu O) and (2 1 4)

    this is done in two stages, first formatting to ensure weights are explicate
    
    example: BaCu3 -> Ba1Cu3

    then parsing into sections

    example: Ba1Cu3 -> Ba, Cu & 1, 3

    '''
    regex = r'([A-Z][a-z](?![0-9]))'
    regex2 = r'([A-Z](?![0-9]|[a-z]))'
    subst = r'\g<1>1'
    for i in range(len(file)):
        file[i] = re.sub(regex, subst, file[i])
        file[i] = re.sub(regex2, subst, file[i])

    elements = np.empty_like(file, dtype=object)
    weights = np.empty_like(file, dtype=object)
    regex3 = r'(\d+\.\d+)|(\d+)'
    for i in range(len(file)):
        parsed = [j for j in re.split(regex3, file[i]) if j]
        elements[i] = parsed[0::2]
        weights[i] = parsed[1::2]
    return elements, weights


def save_file(file, output='output.csv'):
    df = pd.DataFrame.from_records(file)
    df.to_csv(output)


def main(input_file):
    test = load_file(input_file)
    elements, weights = parse_input(test)

    df_list = []
    for i in range(len(elements)):
        df_list.append(look_up(elements[i], weights[i], features='atomic'))

    df = pd.concat(df_list, keys=(x for x in range(len(df_list))))
    print(df)
    save_file(df)
    pass


if __name__ == '__main__':
    # input_file = sys.argv[1]
    main('testfile.txt')
