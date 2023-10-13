from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score


def model(c, d):
    features = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
    target = 'diabetes_mellitus'
    X = c[features] #train data
    Y = c[target]
    Xt = d[features] #test data
    Yt = d[target]
    model = RandomForestClassifier(n_estimators=100, random_state=42) 
    model.fit(X, Y) #to fit the model
    train_predictions = model.predict_proba(X)[:, 1] #to calculate the prob
    test_predictions = model.predict_proba(Xt)[:, 1]
    y_train_pred = model.predict(X) #predict the model
    y_test_pred = model.predict(Xt)
    c['train_predictions'] = train_predictions #add the columns predicted
    d['test_predictions'] = test_predictions
    train_accuracy = accuracy_score(Y, y_train_pred) #calculates the accuracy of the model
    test_accuracy = accuracy_score(Yt, y_test_pred)
    print("Train Accuracy:", train_accuracy)
    print("Test Accuracy:", test_accuracy)
    train_roc_auc = roc_auc_score(Y, train_predictions) #runs roc_auc
    test_roc_auc = roc_auc_score(Yt, test_predictions)
    print("Train ROC AUC:", train_roc_auc)
    print("Test ROC AUC:", test_roc_auc)
    return c, d
   

modeloTra, modeloTes = model(imputed_df, dft1)