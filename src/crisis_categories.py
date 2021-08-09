import numpy as np

# This file allows the characterization of messages according to their crisis. 
# It also consider volcano and landslide hazard types.

#List of 17 crisis types 
list_hazard_type = ['explosion', 'derailment', 'earthquake', 'flood', 'fire', 'meteorite', 
               'wildfires', 'typhoon', 'bombings', 'collapse', 'haze', 'crash', 
               'shooting', 'hurricane', 'tornado', 'cyclone', 'viral_disease', 'volcano', 'landslide']


#list of types of crisis by 'hazard_cat'
list_hazard_cat = ['human_induced', 'natural', 'mixed']

human_induced_types = ['explosion', 'derailment', 'fire', 'bombings', 'collapse', 'crash', 'shooting']
natural_types = ['earthquake', 'flood', 'meteorite', 'wildfires', 'typhoon', 'hurricane', 'tornado', 'cyclone', 'viral_disease','volcano','landslide']
mixed_types = 'haze'


#list of types of crisis by 'hazard_subcat'
list_hazard_subcat = ['accidental', 'geophysical', 'hydrological', 'others', 'climatological', 'meteorological', 'intentional', 'biological']

accidental_types = ['explosion', 'derailment', 'fire', 'collapse', 'crash']
geophysical_types = ['earthquake', 'volcano']
hydrological_types = ['flood', 'landslide']
others_types = ['meteorite', 'haze']
climatological_types = 'wildfires'
meteorological_types = ['typhoon', 'hurricane', 'tornado', 'cyclone']
intentional_types = ['bombings', 'shooting']
biological_types = 'viral_disease'


#list of types of crisis by 'development'
list_development = ['instantaneous', 'progressive']

instantaneous_types = ['explosion', 'derailment', 'earthquake', 'fire', 'meteorite', 'bombings', 'collapse', 'crash', 'shooting', 'landslide']
progressive_types = ['flood', 'wildfires', 'typhoon', 'haze', 'hurricane', 'tornado', 'cyclone', 'viral_disease', 'volcano']


#list of types of crisis by 'spread'
list_spread = ['focalized', 'diffused']

focalized_types = ['explosion', 'derailment', 'fire', 'meteorite', 'bombings', 'collapse', 'crash', 'shooting', 'landslide']
diffused_types = ['earthquake', 'flood', 'wildfires', 'typhoon', 'haze', 'hurricane', 'tornado', 'cyclone', 'viral_disease', 'volcano']



def assign_categ(df):
    """ 
    It creates columns of different crisis categories according to its crisis type 
    """
    df['hazard_cat'] = np.where((df.hazard_type.isin(human_induced_types)), 'human_induced', 
         np.where((df.hazard_type.values == mixed_types), 'mixed', 
                  np.where((df.hazard_type.isin(natural_types)), 'natural', 'unknown')))
    
    df['hazard_subcat'] = np.where((df.hazard_type.isin(geophysical_types)), 'geophysical', 
         np.where((df.hazard_type.isin(hydrological_types)), 'hydrological',
                  np.where((df.hazard_type.values == biological_types), 'biological',  
                           np.where((df.hazard_type.values == climatological_types), 'climatological', 
                                    np.where((df.hazard_type.isin(others_types)), 'others', 
                                             np.where((df.hazard_type.isin(meteorological_types)), 'meteorological',
                                                      np.where((df.hazard_type.isin(intentional_types)), 'intentional',
                                                               np.where((df.hazard_type.isin(accidental_types)), 'accidental', 'unknown'))))))))
    
    df['development'] = np.where((df.hazard_type.isin(instantaneous_types)), 'instantaneous',
                                 np.where((df.hazard_type.isin(progressive_types)), 'progressive', 'unknown'))
    
    df['spread'] = np.where((df.hazard_type.isin(focalized_types)), 'focalized',
                                 np.where((df.hazard_type.isin(diffused_types)), 'diffused', 'unknown'))
    
    return df