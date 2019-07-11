from sklearn import tree
from sklearn import naive_bayes 
from sklearn import neighbors
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
gnb = naive_bayes.GaussianNB()
neigh = neighbors.KNeighborsClassifier()


#[height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

clf = clf.fit(X, Y)
neigh = neigh.fit(X, Y) 
gnb = gnb.fit(X, Y) 


predictionClf = clf.predict([[190, 70, 43],[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]])
predictionNeigh = neigh.predict([[190, 70, 43],[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]])
predictionGnb = gnb.predict([[190, 70, 43],[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]])



print predictionClf == ['male','male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']
print predictionNeigh == ['male','male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']
print predictionGnb == ['male','male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

print accuracy_score(predictionClf, ['male','male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male'])
print accuracy_score(predictionNeigh, ['male','male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male'])
print accuracy_score(predictionGnb, ['male','male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male'])