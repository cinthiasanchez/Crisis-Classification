from sklearn.preprocessing import MinMaxScaler
from src import balance, report
import pandas as pd
import numpy as np

def train_test_split(data, scenario, setting, sampling, max_over, test_sampling=True):
    """
    It splits the training and testing sets not crossing crisis, based on the settings.py file.
    Return: X, X_test, y, y_test
    
    """
    if scenario in ['(a) Monolingual and Mono-Domain', '(b) Monolingual and Cross-Domain', '(d) Cross-lingual and Cross-Domain']:
        #Defining the training set
        mask_train = ((data.hazard_type.isin(setting[0])) &
                      (data.crisis.isin(setting[1]) if len(setting[1]) else True) &
                      (data.lan_final.isin(setting[2])))
        
        mask_test = ((data.hazard_type.isin(setting[3])) &
                     (~data.crisis.isin(setting[4]) if len(setting[4]) else True) &
                     (data.lan_final.isin(setting[5])))
        
    elif scenario in ['(c) Cross-lingual and Mono-Domain', '(e) Cross-lingual and Multi-Domain',
                      '(f) Multi-lingual and Multi-Domain', '(g) Monolingual and Multi-Domain']:
        #Defining the testing set
        mask_train = ((data.hazard_type.isin(setting[0])) &
                      (~data.crisis.isin(setting[1]) if len(setting[1]) else True) &
                      (data.lan_final.isin(setting[2])))
        
        mask_test = ((data.hazard_type.isin(setting[3])) &
                     (data.crisis.isin(setting[4]) if len(setting[4]) else True) &
                     (data.lan_final.isin(setting[5])))
    else:
        print("Error: Scenario doesnt exist")
        
    
    X, y = balance.balance(data[mask_train], sampling, max_over) 
    X_test, y_test = balance.balance_test(data, mask_train, mask_test, setting, 
                                          test_sampling)
    
    return X, X_test, y, y_test


def train_v2(data, columns, scenario, experiment, setting, clf, model, test_sampling=True):
    X, X_test, y, y_test = train_test_split(data, scenario, setting, True, 0.5, test_sampling)
    clf.fit(X[columns], y)
    
    row = dict(scenario=scenario, experiment=experiment, 
               hazard_train='_'.join(setting[0]), 
               lang_train='_'.join(setting[2]),
               train_1=y.value_counts().get(1),
               train_0=y.value_counts().get(0),
               hazard_test='_'.join(setting[3]),
               lang_test='_'.join(setting[5]),
               test_1=y_test.value_counts().get(1),
               test_0=y_test.value_counts().get(0),
               features=model)
    return report.set_experimental_metrics_values(clf, X, X_test, y, y_test, 
                                                  columns, row)
    
          
def train(data, columns, scenario, experiment, setting, clf, model):   
    """
    It trains the classifier using the predictive columns. 
    
    """
    X, X_test, y, y_test = train_test_split(data, scenario, setting, sampling=True, max_over=0.5) #Balance?
    
    clf.fit(X[columns], y)    
    predictions = clf.predict(X_test[columns])       
    final_report, report_ = report.experimental_design(model, clf, X_test, y, y_test, predictions,
                                                       columns, scenario, experiment, setting)
    
    return dict(**final_report, **report_)



def scale_numeric_features(X, X_test, numeric_features, scale):
    if scale:
        scaler = MinMaxScaler()
        X[numeric_features] = scaler.fit_transform(X[numeric_features])
        X_test[numeric_features] = scaler.transform(X_test[numeric_features])
        return X, X_test
    return X, X_test 