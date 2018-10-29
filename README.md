# magpy
This package has been written to to copy the behaviour of [MAGPIE](http://oqmd.org/static/analytics/magpie/doc/)'s elemental feature lookup for materials infomatics in Python.

Example usage:

```
from magpie import parse_input, look_up

input = ['NaCl', 'H2SO4', 'C2H4']
elements, weights = parse_input(input)
features=['ElectronAffinity', 'Electronegativity']
df_list = look_up(elements, weights, features)
stat_list = get_descriptors(df_list, features)
print(combine_dfs(df_list))
print(combine_dfs(stat_list))
```
