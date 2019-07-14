# Pre-req: Run pip3 install virtualenv
# Before running this script, for optimal efficiency, make sure
# you are inside a virtualenv by running source env/bin/activate

echo "Download Data Science Libaries"
pip3 install numpy
pip3 install scipy
pip3 install pandas
pip3 install scikit-learn

echo "Donwload Communication Libraries"
pip3 install requests

echo "Downloading Jupyter"
pip3 install jupyter

echo "Download AI Libraries"
pip3 install tensorflow

echo "Extra Libraries"
pip3 install click
