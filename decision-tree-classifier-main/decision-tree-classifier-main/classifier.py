# Innitial delve into Data Science using Python

from sklearn import tree

#[height, weight, shoe size]
X = [[181,80,44], [177,70,43], [160, 60, 38], [166,65,40], [190,90,47],
      [177,71,41], [181,85,43], [171,75,42], [165, 55, 25], [159, 45, 36],
        [195, 90, 51]]

Y = ['male', 'female', 'male', 'female' , 'female', 'male', 'male', 'female',
      'female', 'male', 'female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[190,70,43]])

print(prediction[0])
