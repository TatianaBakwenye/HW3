from sklearn.model_selection import train_test_split


def splitdata(df):
    X = df.drop('diabetes_mellitus', axis=1)
    y = df['diabetes_mellitus']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test