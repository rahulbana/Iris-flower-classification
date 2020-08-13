# Iris-flower-classification
IRIS Flower Classification [https://irisflowerml.herokuapp.com/](https://irisflowerml.herokuapp.com/){:target="_blank" rel="noopener"}

You can deploy this solution directly on heroku.

## Requirement
Python 3.6.6 

#### Steps to run local
git clone https://github.com/rahulbana/Iris-flower-classification.git

cd Iris-flower-classification

pip install -r requirements.txt

pip jupyter notebook

run full notebook to create model file

python app.py


#### Steps to run on heroku
git clone https://github.com/rahulbana/Iris-flower-classification.git

cd Iris-flower-classification

pip install -r requirements.txt

pip jupyter notebook

run full notebook to create model file

git init

heroku login

heroku create <project_name>

git add .

git commit -m "initial commit"

git push heroku master
