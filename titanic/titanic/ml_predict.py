def prediction_model(pclass,sex, age, sibSp, parch, fare, embarked, title):
    import pickle
    x = [[pclass,sex, age, sibSp, parch, fare, embarked, title]]
    randomforest = pickle.load(open('titanic_model.sav', 'rb'))
    prediction = randomforest.predict(x)
    if prediction == [1]:
        return "Survived"
    elif prediction == [0]:
        return "Not Survived"
    else:
        return "Error"
    return prediction
