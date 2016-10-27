from __future__ import division
import pickle


enron_data = pickle.load(open("../tools/final_project_dataset.pkl", "r"))

print enron_data['SKILLING JEFFREY K']

print "Total length of dataset"
print len(enron_data)


print "Total Attributes per person"
print len(enron_data[enron_data.keys()[0]])




print "Percentage NAN for their total payments"
count =0
for key, d in enron_data.iteritems():
     if d['total_payments'] == 'NaN':
     	count+=1
print (count/len(enron_data))*100


counts_poi=[0,0]
for key, d in enron_data.iteritems():
     if d['total_payments'] == 'NaN' and d['poi'] == True:
             counts_poi[0] += 1
     elif d['poi'] == True:
             counts_poi[1] += 1

print ("Total percentage of POI who has NAN total_payment")
print (counts_poi[0]/len(enron_data))*100


print "Total_payment = NAN and totalPoint of interest"
print counts_poi