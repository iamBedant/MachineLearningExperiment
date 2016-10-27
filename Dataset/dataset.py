import pickle

enron_data = pickle.load(open("../tools/final_project_dataset.pkl", "r"))

print enron_data['SKILLING JEFFREY K']
print len(enron_data)
print len(enron_data[enron_data.keys()[0]])

counts_poi=[0,0]

for key, d in enron_data.iteritems():
     if d['total_payments'] == 'NaN' and d['poi'] == True:
             counts_poi[0] += 1
     elif d['poi'] == True:
             counts_poi[1] += 1

print counts_poi
