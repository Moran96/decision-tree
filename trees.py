from math import log

#calculate the shannon entropy.
def calculate_shannon_entropy(data_set):
	num_entries = len(data_set)
	label_counts = {}
	for feat_vec in data_set:
		current_label = feat_vec[-1]
		if current_label not in label_counts.keys():
			label_counts[current_label] = 0
			label_counts[current_label] += 1
		else:
			label_counts[current_label] +=1
		#test
		print(current_label)
		print(label_counts)
	shannon_entropy = 0.0
	for key in label_counts:
		prob = float(label_counts[key])/num_entries
		shannon_entropy -= prob * log(prob,2)
	return shannon_entropy

def create_data_set():
	data_set = [[1,1,'yes'],
	[1,1,'yes'],
	[1,0,'no'],
	[0,1,'no'],
	[0,1,'no']]
	labels = ['no surfacing','flippers']
	return data_set,labels
