import pandas as pd
from sklearn import preprocessing
import pprint

def get_features(data,classifier_type="C"):
    if classifier_type=="C":
        y_label = 'label'
    else:
        y_label = 'score'
    grouped = data.groupby('video')
    X = []
    y = []
    for video, group in grouped:
        X_person = []
        y_person = []
        for i in range(len(group)):
            X_person.append(group.iloc[i].tolist()[1:-2])
            y_person.append(group.iloc[i]['label'])
        X.append(X_person)
        y.append(y_person)
    return X,y

def features(mode,classifier,split,problem_type='C',normalize="regular"):
    if mode == "visual":
        file = "data/selected_features/"+normalize+"/"+split+"/"+classifier+"_visual_"+split+".csv"
    elif mode == "acoustic":
        file = "data/selected_features/"+normalize+"/"+split+"/"+classifier+"_acoustic_"+split+".csv"
    elif mode == "linguistic":
        file = "data/selected_features/"+normalize+"/"+split+"/"+classifier+"_linguistic_"+split+".csv"
    data = pd.read_csv(file)
    return get_features(data,problem_type)
