import sys
import pickle
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../tools/final_project_dataset.pkl", "r") )

### list the features you want to look at--first item in the
### list will be the "target" feature

features_list = ["bonus", "salary"]

print dictionary


data = featureFormat( dictionary, features_list, remove_any_zeroes=True)

# print data