from django.shortcuts import render
from . import checkName
from . import fake_modle
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    Pclass = int(request.GET['Pclass'])
    Sex = int(request.GET['Sex'])
    Age = int(request.GET['Age'])
    SibSp = int(request.GET['SibSp'])
    Parch = int(request.GET['Parch'])
    Fare = int(request.GET['Fare'])
    Embarked = int(request.GET['Embarked'])
    title = int(request.GET['title'])
    #user_input = checkName.checkName(user_input)
    prediction = ml_predict.prediction_model(Pclass,Sex, Age, SibSp, Parch, Fare, Embarked, title)
    return render(request, 'result.html', {'prediction': prediction})
