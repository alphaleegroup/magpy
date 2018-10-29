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

from magpy import *


def test(feature_file, composition_file):
    features = load_file(feature_file)
    compositions = load_file(composition_file)
    elements, weights = parse_input(compositions)

    df_list = look_up(elements, weights, features=features)
    df = combine_dfs(df_list)
    print(df)


    stats_list = get_descriptors(df_list, features)
    stats = combine_dfs(stats_list)
    print(stats)

    pass


if __name__ == '__main__':
    feature_file = sys.path[0] + '/featuretest.txt'
    composition_file = sys.path[0] + '/compositiontest.txt'
    test(feature_file, composition_file)
