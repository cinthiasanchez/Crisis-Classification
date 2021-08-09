
EN_quake_crisis = ['earthquake_Bohol', 'earthquake_California', 'earthquake_Chile',
                   'earthquake_CostaRica', 'earthquake_Ecuador', 'earthquake_Guatemala',
                   'earthquake_Iraq_Iran', 'earthquake_Italy', 'earthquake_Mexico',
                   'earthquake_Nepal', 'earthquake_Pakistan']

EN_explosion_crisis = ['explosion_WestTexas']
EN_flood_crisis = ['flood_Alberta', 'flood_Colorado', 'flood_India', 'flood_Manila',
                   'flood_Pakistan', 'flood_Philippines', 'flood_Queensland',
                   'flood_Sardinia', 'flood_SriLanka']

ES_quake_crisis = ['earthquake_Chile', 'earthquake_Ecuador', 'earthquake_Guatemala', 'earthquake_CostaRica']
IT_quake_crisis = ['earthquake_Italy', 'earthquake_Laquila']
ES_explosion_crisis = ['explosion_Venezuela']    
IT_flood_crisis = ['flood_Genova', 'flood_Sardinia']

source_EN_flood = 'flood_Alberta'
source_EN_quake = 'earthquake_Nepal'
source_ES_quake = 'earthquake_Chile'
source_IT_quake = 'earthquake_Italy'   

def experimental_design():
    """
    Build a dictionary with the experimental setup. 
    It is composed of scenarios and experiments. 
    According to it, classification.py splits the training and testing sets.
    
    Note: For Spanish and Italian targets, we define the crisis events to exclude them from the training set 
    and thus avoid any cross. 
    """ 
    
    experiments = dict()
    #format for a,b,d scenarios (hazard_train,  crisis_train, lang_train, hazard_test, ~crisis_test, lang_test)
    #format for c,e,f,g scenarios (hazard_train, ~crisis_train, lang_train, hazard_test,  crisis_test, lang_test)

    ########## (a) Mono-lingual and Mono-domain ###########    
    experiments['(a) Monolingual and Mono-Domain'] = dict(EN_flood=(['flood'], [source_EN_flood], ['en'],
                                                         ['flood'], [source_EN_flood], ['en']))
    
    experiments['(a) Monolingual and Mono-Domain']['EN_quake'] =(['earthquake'], [source_EN_quake], ['en'],
                                                      ['earthquake'], [source_EN_quake], ['en'])

    experiments['(a) Monolingual and Mono-Domain']['ES_quake'] = (['earthquake'], [source_ES_quake], ['es'],
                                                       ['earthquake'], [source_ES_quake], ['es'])    

    experiments['(a) Monolingual and Mono-Domain']['IT_quake'] = (['earthquake'], [source_IT_quake], ['it'],
                                                       ['earthquake'], [source_IT_quake], ['it'])
    

    ########## (b) Mono-lingual and Cross-domain ###########
    experiments['(b) Monolingual and Cross-Domain'] = dict(EN_expl=(['earthquake', 'flood'], [], ['en'],
                                                         ['explosion'], [], ['en']))      
                                                
    experiments['(b) Monolingual and Cross-Domain']['EN_flood'] = (['explosion', 'earthquake'], [], ['en'],
                                                        ['flood'], [source_EN_flood], ['en'])
                                                
    experiments['(b) Monolingual and Cross-Domain']['EN_quake'] = (['explosion', 'flood'], [], ['en'],
                                                        ['earthquake'], [source_EN_quake], ['en']) 
    
    experiments['(b) Monolingual and Cross-Domain']['ES_expl'] = (['earthquake'], [], ['es'],
                                                       ['explosion'], [], ['es'])
                                                
    experiments['(b) Monolingual and Cross-Domain']['ES_quake'] = (['explosion'], [], ['es'],
                                                        ['earthquake'], [source_ES_quake], ['es'])        
    
    experiments['(b) Monolingual and Cross-Domain']['IT_flood'] = (['earthquake'], [], ['it'],
                                                        ['flood'], [], ['it'])
    
    experiments['(b) Monolingual and Cross-Domain']['IT_quake'] = (['flood'], [], ['it'],
                                                        ['earthquake'], [source_IT_quake], ['it'])                                          
    

    ########## (c) Cross-lingual and Mono-domain ###########    
                                                
    experiments['(c) Cross-lingual and Mono-Domain'] = dict(ES_expl=(['explosion'], ES_explosion_crisis, ['en'],
                                                        ['explosion'], ES_explosion_crisis, ['es']))  
                                                
    experiments['(c) Cross-lingual and Mono-Domain']['IT_flood'] = (['flood'], IT_flood_crisis, ['en'],
                                                       ['flood'], IT_flood_crisis, ['it'])
                                              
    experiments['(c) Cross-lingual and Mono-Domain']['ES_quake'] = (['earthquake'], ES_quake_crisis, ['en'],
                                                       ['earthquake'], [x for x in ES_quake_crisis if x != source_ES_quake], ['es'])

    experiments['(c) Cross-lingual and Mono-Domain']['IT_quake'] = (['earthquake'], IT_quake_crisis, ['en'],
                                                       ['earthquake'], [x for x in IT_quake_crisis if x != source_IT_quake], ['it'])    
    
    
    ########## (d) Cross-lingual and Cross-domain ###########                                                  
    experiments['(d) Cross-lingual and Cross-Domain'] = dict(ES_expl=(['earthquake', 'flood'], [], ['en'],
                                                         ['explosion'], [], ['es']))  
    
    experiments['(d) Cross-lingual and Cross-Domain']['IT_flood'] = (['explosion', 'earthquake'], [], ['en'],
                                                        ['flood'], [], ['it'])   
       

    experiments['(d) Cross-lingual and Cross-Domain']['ES_quake'] = (['explosion', 'flood'], [], ['en'],
                                                        ['earthquake'], [source_ES_quake], ['es'])
    
    experiments['(d) Cross-lingual and Cross-Domain']['IT_quake'] = (['explosion', 'flood'], [], ['en'],
                                                        ['earthquake'], [source_IT_quake], ['it'])    
    

    ########## (e) Cross-lingual and Multi-domain ###########
    experiments['(e) Cross-lingual and Multi-Domain'] = dict(ES_expl=(['explosion', 'earthquake', 'flood'], ES_explosion_crisis, ['en'],
                                                          ['explosion'], ES_explosion_crisis, ['es']))     
    
    experiments['(e) Cross-lingual and Multi-Domain']['IT_flood'] = (['explosion', 'earthquake', 'flood'], IT_flood_crisis, ['en'],
                                                         ['flood'], IT_flood_crisis, ['it'])   

    experiments['(e) Cross-lingual and Multi-Domain']['ES_quake'] = (['explosion', 'earthquake', 'flood'], ES_quake_crisis, ['en'],
                                                         ['earthquake'], [x for x in ES_quake_crisis if x != source_ES_quake], ['es'])

    experiments['(e) Cross-lingual and Multi-Domain']['IT_quake'] = (['explosion', 'earthquake', 'flood'], IT_quake_crisis, ['en'],
                                                         ['earthquake'], [x for x in IT_quake_crisis if x != source_IT_quake], ['it'])
    
    
    
    ########## (f) Multi-lingual and Multi-domain ###########
    experiments['(f) Multi-lingual and Multi-Domain'] = dict(ES_expl=(['explosion', 'earthquake', 'flood'], 
                                                                      ES_explosion_crisis, ['en', 'es'],
                                                                      ['explosion'], ES_explosion_crisis, ['es']))     
    
    experiments['(f) Multi-lingual and Multi-Domain']['IT_flood'] = (['explosion', 'earthquake', 'flood'], 
                                                                     IT_flood_crisis, ['en', 'it'],
                                                                     ['flood'], IT_flood_crisis, ['it'])   


    experiments['(f) Multi-lingual and Multi-Domain']['ES_quake'] = (['explosion', 'earthquake', 'flood'], 
                                                                     [x for x in ES_quake_crisis if x != source_ES_quake], ['en', 'es'],
                                                                     ['earthquake'], [x for x in ES_quake_crisis if x != source_ES_quake], ['es'])

    experiments['(f) Multi-lingual and Multi-Domain']['IT_quake'] = (['explosion', 'earthquake', 'flood'], 
                                                                     [x for x in IT_quake_crisis if x != source_IT_quake], ['en', 'it'],
                                                                     ['earthquake'], [x for x in IT_quake_crisis if x != source_IT_quake], ['it'])
    
    
    ########## (g) Mono-lingual and Multi-domain for English ###########
    experiments['(g) Monolingual and Multi-Domain'] = dict(EN_expl=(['explosion', 'earthquake', 'flood'], EN_explosion_crisis, ['en'],
                                                                    ['explosion'], EN_explosion_crisis, ['en']))      
                                                
    experiments['(g) Monolingual and Multi-Domain']['EN_flood'] = (['explosion', 'earthquake', 'flood'], 
                                                                   [x for x in EN_flood_crisis if x != source_EN_flood], ['en'],
                                                                   ['flood'], [x for x in EN_flood_crisis if x != source_EN_flood], ['en'])
                                                
    experiments['(g) Monolingual and Multi-Domain']['EN_quake'] = (['explosion', 'earthquake', 'flood'], 
                                                                   [x for x in EN_quake_crisis if x != source_EN_quake], ['en'],
                                                                   ['earthquake'], [x for x in EN_quake_crisis if x != source_EN_quake], ['en']) 


    return experiments
