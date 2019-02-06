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


import magpy


def main():
    feature_file = 'inputs/features.dat'
    features = magpy.load_file(feature_file)

    composition_file = 'inputs/compositions.dat'
    compositions = magpy.load_file(composition_file)
    elements, weights = magpy.parse_input(compositions)

    df_list = magpy.look_up(elements, weights, features=features)
    df = magpy.combine_dfs(df_list)
    print(df, '\n')

    stats_list = magpy.get_descriptors(df_list, features=features)
    stats = magpy.combine_dfs(stats_list)
    print(stats, '\n')

    pass

if __name__ == '__main__':
    main()
