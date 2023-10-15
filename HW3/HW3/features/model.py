from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score


def model(X_train, X_test, y_train, y_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    train_predictions = model.predict_proba(X_train)[:, 1]
    test_predictions = model.predict_proba(X_test)[:, 1]
    X_train['predictions'] = train_predictions
    X_test['predictions'] = test_predictions
    train_roc_auc = roc_auc_score(y_train, train_predictions)
    test_roc_auc = roc_auc_score(y_test, test_predictions)
    
    print("Train ROC AUC:", train_roc_auc)
    print("Test ROC AUC:", test_roc_auc)
    
    return train_roc_auc, test_roc_auc