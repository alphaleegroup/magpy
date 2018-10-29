import numpy as np
import pandas as pd

def construct_dict(feature):
    with open('tables/' + feature + '.txt') as f:
        d = dict(x.rstrip().split(None, 1) for x in f)
    return d

def look_up(elements, weights, features='atomic', feature_list=[]):
    '''
    allowed features:
        'AtomicVolume', 'AtomicWeight', 'BoilingT', 'BoilingTemp', 
        'BulkModulus', 'Column', 'CovalentRadius', 'Density', 
        'ElectronAffinity', 'Electronegativity', 'FirstIonizationEnergy', 
        'FusionEnthalpy', 'GSbandgap', 'GSenergy_pa', 'GSestBCClatcnt', 
        'GSestFCClatcnt', 'GSmagmom', 'GSvolume_pa', 'HHIp', 'HHIr', 
        'HeatCapacityMass', 'HeatCapacityMolar', 'HeatFusion', 'ICSDVolume', 
        'IsAlkali', 'IsDBlock', 'IsFBlock', 'IsMetal', 'IsMetalloid', 
        'IsNonmetal', 'MeltingT', 'MendeleevNumber', 'MiracleRadius', 
        'NUnfilled', 'NValance', 'NdUnfilled', 'NdValence', 'NfUnfilled', 
        'NfValence', 'NpUnfilled', 'NpValence', 'NsUnfilled', 'NsValence', 
        'Number', 'Polarizability', 'Row', 'ShearModulus', 'SpaceGroupNumber', 
        'Wigner', 'ZungerPP-r_d', 'ZungerPP-r_p', 'ZungerPP-r_pi', 
        'ZungerPP-r_s', 'ZungerPP-r_sigma'
    '''
    if features == 'atomic':
        feature_list = ['CovalentRadius', 'Polarizability', 'Electronegativity',
                         'FirstIonizationEnergy', 'ElectronAffinity' ]
        collect_values(elements, weights, feature_list)
    elif features == 'all':
        feature_list = ['AtomicVolume', 'AtomicWeight', 'BoilingT', 'BoilingTemp', 
                        'BulkModulus', 'Column', 'CovalentRadius', 'Density', 
                        'ElectronAffinity', 'Electronegativity', 'FirstIonizationEnergy', 
                        'FusionEnthalpy', 'GSbandgap', 'GSenergy_pa', 'GSestBCClatcnt', 
                        'GSestFCClatcnt', 'GSmagmom', 'GSvolume_pa', 'HHIp', 'HHIr', 
                        'HeatCapacityMass', 'HeatCapacityMolar', 'HeatFusion', 'ICSDVolume', 
                        'IsAlkali', 'IsDBlock', 'IsFBlock', 'IsMetal', 'IsMetalloid', 
                        'IsNonmetal', 'MeltingT', 'MendeleevNumber', 'MiracleRadius', 
                        'NUnfilled', 'NValance', 'NdUnfilled', 'NdValence', 'NfUnfilled', 
                        'NfValence', 'NpUnfilled', 'NpValence', 'NsUnfilled', 'NsValence', 
                        'Number', 'Polarizability', 'Row', 'ShearModulus', 'SpaceGroupNumber', 
                        'Wigner', 'ZungerPP-r_d', 'ZungerPP-r_p', 'ZungerPP-r_pi', 
                        'ZungerPP-r_s', 'ZungerPP-r_sigma']
        collect_values(elements, weights, feature_list)
    elif features == 'custom':
        if not feature_list:
            raise('InputError: No Features to evaluate in \'feature_list\'')
        collect_values(elements, weights, feature_list)
    else:
        raise('InputError: No Features Given, specify \'features\' kwarg')

def collect_values(elements, weights, feature_list):
    output = np.column_stack((elements,weights))
    for feature in feature_list:
        d = construct_dict(feature)
        values = np.vectorize(d.get)(elements)
        output = np.column_stack((output,values))
    df = pd.DataFrame(output,columns=['Element','Weights']+feature_list)
    return df



def main():
    print('I am not a run script, try magpy.py')
    pass


if __name__ == '__main__':
    main()
