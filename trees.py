from math import log

#Calculate the shannon entropy.
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
		# print(current_label)
		# print(label_counts)
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

#Split the dataset by the attribute that appointed.
def split_data_set(dataset,axis,value):
	return_data_set = []
	for feat_vec in dataset:
		if feat_vec[axis] == value:
			reduced_feat_vec = feat_vec[:axis]
			reduced_feat_vec.extend(feat_vec[axis+1:])
			return_data_set.append(reduced_feat_vec)
	return return_data_set

def choose_best_split(dataset):
	num_features = len(dataset[0]) - 1
	base_entropy = calculate_shannon_entropy(dataset)
	best_info_gain = 0.0
	best_feature = -1

	for i in range(num_features):
		list_feat = [example[i] for example in dataset]    #choose axis of a dataset
		unique_vals = set(list_feat)
		new_entropy = 0.0
		for value in unique_vals:
			sub_data_set = split_data_set(dataset,i,value)
			prob = len(sub_data_set)/float(len(dataset))
			new_entropy += prob * calculate_shannon_entropy(sub_data_set)

			info_gain = base_entropy - new_entropy
			print("row=",i,"value=",value,'\t',"new_entropy=",new_entropy,'\t',"info_gain=",info_gain)	

			if(info_gain > best_info_gain):
				best_info_gain = info_gain
				best_feature = i
	return best_feature