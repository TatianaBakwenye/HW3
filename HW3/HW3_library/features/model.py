from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score

#function that trains a random forrest model
def model(train_data, test_data, features, target):
    X_train = train_data[features] #train data
    Y_train = train_data[target]
    X_test = test_data[features] #test data
    Y_test = test_data[target]
    model = RandomForestClassifier(n_estimators=100, random_state=42) 
    model.fit(X_train, Y_train) #to fit the model
    train_predictions = model.predict_proba(X_train)[:, 1] #to calculate the prob
    test_predictions = model.predict_proba(X_test)[:, 1]
    y_train_pred = model.predict(X_train) #predict the model
    y_test_pred = model.predict(X_test)
    train_data['train_predictions'] = train_predictions #add the columns predicted
    test_data['test_predictions'] = test_predictions
    train_accuracy = accuracy_score(Y_train, y_train_pred) #calculates the accuracy of the model
    test_accuracy = accuracy_score(Y_test, y_test_pred)
    print("Train Accuracy:", train_accuracy)
    print("Test Accuracy:", test_accuracy)
    train_roc_auc = roc_auc_score(Y_train, train_predictions) #runs roc_auc
    test_roc_auc = roc_auc_score(Y_test, test_predictions)
    print("Train ROC AUC:", train_roc_auc)
    print("Test ROC AUC:", test_roc_auc)
    return train_data, test_data
