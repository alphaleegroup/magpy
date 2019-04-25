import magpy

compositions = ['La2CuO4', 'NaCl', 'H2O']

data = magpy.core.descriptors(compositions, embedding_file="/home/rhys/work/magpy/notebooks/elem_low_embedding.json")

print(data.shape)