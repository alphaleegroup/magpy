# magpy
Elemental feature lookup for materials infomatics

Example usage:

```
from magpie import parse_input, look_up

input = ['NaCl', 'H2SO4', 'C2H4']
elements, weights = parse_input(input)
df_list = look_up(elements, weights, features=['ElectronAffinity', 
                                            'Electronegativity'])
print(combine_dfs(df_list))
```
