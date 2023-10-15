from sklearn.model_selection import train_test_split


def splitdata(x):
    traindf, testdf = train_test_split(x, test_size=0.4, random_state=42) #takes the data and splits it 40% to test
    traindf = traindf.reset_index(drop=True) #to reset the index to 0
    testdf = testdf.reset_index(drop=True)
    return traindf, testdf