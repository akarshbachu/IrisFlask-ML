import sklearn
import sklearn.datasets
import sklearn.ensemble
import pickle


iris = sklearn.datasets.load_iris()

train, test, label_train, label_test = sklearn.model_selection.train_test_split(iris.data, iris.target, test_size=0.2)

rf = sklearn.ensemble.RandomForestClassifier()
rf.fit(train,label_train)

pickle_out = open('iris_rf_model','wb')
pickle.dump(rf,pickle_out)
pickle_out.close()

print('Model Score: ', rf.score(test,label_test))