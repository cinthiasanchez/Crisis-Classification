from imblearn.over_sampling import RandomOverSampler
import pandas as pd

def balance(train, sampling=False, max_over=0.5):
    """
    It balances the training data (if the parameter sampling=True). 
    It receives the parameter max_over indicating the maximum 
    proportion of instances to oversample of the minority class. 
    """
    if sampling:        
        return over_sub(train, max_over)  
    return train, train.label


def balance_test(data, mask_train, mask_test, setting, sampling=False):
    """
    It balances the test data (if the parameter sampling=True) when 
    the majority class is the positive (related to crisis). 
    Balancing the test sets involves adding noise, 
    i.e., messages of the negative class (not related to crisis).
    """
    
    if not sampling:
        return data[mask_test], data[mask_test].label
    
    mask = ~data.hazard_type.isin(['earthquake', 'flood', 'explosion'])
    options = data[(~(mask_train | mask_test) & (data.label == 0) & 
                    data.lan_final.isin(setting[5]) & mask)]
    neg = data[mask_test].label.value_counts().get(0)
    n_sample = len(data[mask_test]) - 2 * neg
    if n_sample < 1:
        return data[mask_test], data[mask_test].label
    
    samples = options.sample(n_sample)
    subset = pd.concat([data[mask_test], samples], ignore_index=True)
    return subset, subset.label
    
        
    
def over_sub(train, max_over):
    class1 = train[train.label==1]
    class0 = train[train.label==0]
    limit_0 = int(len(class0) + len(class0) * max_over)
    limit_1 = int(len(class1) + len(class1) * max_over)
    
    if len(class1) == len(class0):
        X_bal, y_bal = train, train.label
        
    elif len(class1) > len(class0):
        X_bal, y_bal = oversampling(train, class1, class0, limit_0)
        
    elif len(class0) > len(class1):
        X_bal, y_bal = oversampling(train, class0, class1, limit_1)
        
    return X_bal, y_bal


def oversampling(train, classmax, classmin, limit):
    # balanced sampling max_over % of minority class
    if len(classmax) <= limit:
        oversample = RandomOverSampler(sampling_strategy='minority') 
        X_bal, y_bal = oversample.fit_resample(train, train.label)
    
    # reduce majority class before oversampled minority class
    else:
        classmax_sub = classmax.sample(limit) # random_state=1
        train_sub = pd.concat([classmin, classmax_sub])
        
        oversample = RandomOverSampler(sampling_strategy='minority') 
        X_bal, y_bal = oversample.fit_resample(train_sub, train_sub.label)    
    return X_bal, y_bal