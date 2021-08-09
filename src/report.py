from src import classification
import pandas as pd
import numpy as np
from sklearn.metrics import (confusion_matrix, cohen_kappa_score, classification_report,
                             precision_score, recall_score, f1_score, roc_auc_score,
                             accuracy_score, roc_curve)

def experimental_design(model, clf, X_test, y, y_test, predictions, columns, scenario, experiment, setting):
    """
    Build a classification report for every experiment.
    """
    
    cohen_kappa = cohen_kappa_score(y_test, predictions)     
    pre_micro = precision_score(y_test, predictions, average='micro')
    rec_micro = recall_score(y_test, predictions, average='micro')
    f1sc_micro = f1_score(y_test, predictions, average='micro')
    f1sc_binary = f1_score(y_test, predictions, average='binary')
    report = classification_report(y_test, predictions, output_dict=True)
    report = dict(pd.json_normalize(report, sep='_').iloc[0])    
    
    final_report = dict(
        scenario=scenario,
        experiment=experiment,
        hazard_train='_'.join(setting[0]),
        lang_train='_'.join(setting[2]), 
        train_1=y.value_counts().get(1),
        train_0=y.value_counts().get(0),
        hazard_test='_'.join(setting[3]),
        lang_test='_'.join(setting[5]),
        test_1=y_test.value_counts().get(1),
        test_0=y_test.value_counts().get(0),
        features=model,
        kappa=cohen_kappa,
        P_micro=pre_micro,
        R_micro=rec_micro,
        F1_micro=f1sc_micro,
        F1_binary=f1sc_binary, 
        probs_predict=clf.predict_proba(X_test[columns]),
        predictions=predictions,
        label_true=y_test.values
    )
    
    return final_report, report

def compute_score_threshold(probs, y, fn_metric, kw):
    thresholds = np.arange(0, 1.01, 0.05)
    scores = [fn_metric(y, (probs >= th) * 1, **kw)
              for th in thresholds]
    ix = np.argmax(scores)
    baseline = fn_metric(y, (probs >= .5) * 1, **kw)
    return baseline, scores[ix], thresholds[ix]


def compute_youden_th(probs, y):
    fp, tp, thresholds = roc_curve(y, probs)
    return thresholds[np.argmax(tp - fp)]

def set_values_container(probs, y, row, k):
    row[f'{k}_prec'], row[f'{k}_top_prec'] , row[f'{k}_th_prec'] = (
        compute_score_threshold(probs, y, precision_score, {'average':'binary'}))
    row[f'{k}_rec'], row[f'{k}_top_rec'] , row[f'{k}_th_rec'] = (
        compute_score_threshold(probs, y, recall_score, {'average':'binary'}))
    row[f'{k}_f1'], row[f'{k}_top_f1'] , row[f'{k}_th_top_f1'] = (
        compute_score_threshold(probs, y, f1_score, {'average':'binary'}))
    
    row[f'{k}_prec_macro'], row[f'{k}_top_prec_macro'] , row[f'{k}_th_prec_macro'] = (
        compute_score_threshold(probs, y, precision_score, {'average':'macro'}))
    row[f'{k}_rec_macro'], row[f'{k}_top_rec_macro'] , row[f'{k}_th_rec_macro'] = (
        compute_score_threshold(probs, y, recall_score, {'average':'macro'}))
    row[f'{k}_f1_macro'], row[f'{k}_top_f1_macro'] , row[f'{k}_th_top_f1_macro'] = (
        compute_score_threshold(probs, y, f1_score, {'average':'macro'}))
    
    row[f'{k}_prec_micro'], row[f'{k}_top_prec_micro'] , row[f'{k}_th_prec_micro'] = (
        compute_score_threshold(probs, y, precision_score, {'average':'micro'}))
    row[f'{k}_rec_micro'], row[f'{k}_top_rec_micro'] , row[f'{k}_th_rec_micro'] = (
        compute_score_threshold(probs, y, recall_score, {'average':'micro'}))
    row[f'{k}_f1_micro'], row[f'{k}_top_f1_micro'] , row[f'{k}_th_top_f1_micro'] = (
        compute_score_threshold(probs, y, f1_score, {'average':'micro'}))
    
    row[f'{k}_kappa'], row[f'{k}_top_kappa'] , row[f'{k}_th_kappa'] = (
        compute_score_threshold(probs, y, cohen_kappa_score, {}))
    
    row[f'{k}_youden'] = compute_youden_th(probs, y)
    
    
def compute_metrics(clf, x, y, row, k='train'):
    prob = clf.predict_proba(x)[:, 1]
    row[f'{k}_auc'] = roc_auc_score(y, prob)
    if k == 'train':
        row[f'{k}_f1'] = f1_score(y, (prob >= .5) *1.)
        row[f'{k}_f1_macro'] = f1_score(y, (prob >= .5) *1., average='macro')
        return
    set_values_container(prob, y, row, k)
    return prob


def extra_metrics(y_test, prediction):
    report = classification_report(y_test, prediction,
                                   output_dict=True)
    report = dict(pd.json_normalize(report, sep='_').iloc[0])
    return (report['0_precision'], report['1_precision'], 
            report['0_recall'], report['1_recall'], 
            report['0_f1-score'], report['1_f1-score'], 
            report['macro avg_f1-score'], report['accuracy']
           )

       
    
def set_experimental_metrics_values(clf, X, X_test, y, y_test, columns, row):
    compute_metrics(clf, X[columns], y, row, k='train')
    probs = compute_metrics(clf, X_test[columns], y_test, row, k='test')   
    row['prec_0'], row['prec_1'], row['rec_0'], row['rec_1'], row['f1_0'], row['f1_1'], row['f1_macro'], row['accuracy'] = extra_metrics(y_test, (probs >= .5) * 1.)
    
    row['prec_kappa_0'], row['prec_kappa_1'], row['rec_kappa_0'], row['rec_kappa_1'], row['f1_kappa_0'], row['f1_kappa_1'], row['f1_kappa_macro'], row['accuracy_kappa'] = extra_metrics(
        y_test, (probs >= row['test_th_kappa']) * 1)
    
    row['prec_youden_0'], row['prec_youden_1'], row['rec_youden_0'], row['rec_youden_1'], row['f1_youden_0'], row['f1_youden_1'], row['f1_youden_macro'], row['accuracy_youden'] = extra_metrics(y_test, (probs >= row['test_youden']) * 1)
    
    cond = row['test_1'] >= row['test_0']
    dummy = np.ones(len(y_test)) if cond else np.zeros(len(y_test))
    row['prec_dummy_0'], row['prec_dummy_1'], row['rec_dummy_0'], row['rec_dummy_1'], row['f1_dummy_0'], row['f1_dummy_1'], row['f1_dummy_macro'], row['accuracy_dummy'] = extra_metrics(y_test, dummy)
    return row
