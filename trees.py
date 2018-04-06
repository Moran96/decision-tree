from math import log
import operator

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

def majority_cnt(class_list):
	class_count = {}
	for vote in class_list:
		if vote not in class_count.keys(): class_count[vote] = 0
		class_count[vote] += 1
	sorted_class_count = sorted(class_count.iteritems(),
		key = operator.itemgetter(1),reverse=True)
	return sorted_class_count[0][0]

#Create tree
def create_tree(dataset,labels):
	class_list = [example[-1] for example in dataset]
	if class_list.count(class_list[0]) == len(class_list):
		return class_list[0]
	if len(dataset[0]) == 1:
		return majority_cnt(class_list)
	best_feature = choose_best_split(dataset)
	best_feature_label = labels[best_feature]

	my_tree = {best_feature_label:{}}
	del(labels[best_feature])
	feat_values = [example[best_feature] for example in dataset]
	unique_vals = set(feat_values)
	for value in unique_vals:
		sub_labels = labels[:]
		my_tree[best_feature_label][value] = create_tree(split_data_set\
			(dataset,best_feature,value),sub_labels)
	return my_tree

#-------