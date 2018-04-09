import matplotlib.pyplot as plt

decision_on_node = dict(boxstyle="sawtooth", fc="0.8")
leaf_node = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

def plot_node(node_txt,center_pt,parent_pt,node_type):
	create_plot.ax1.annotate(node_txt,xy=parent_pt,xycoords='axes fraction',
		xytext=center_pt,textcoords='axes fraction',
		va="center",ha="center",bbox=node_type,arrowprops=arrow_args)

def create_plot():
	fig = plt.figure(1,facecolor='white')
	fig.clf()
	create_plot.ax1 = plt.subplot(111,frameon=False)
	plot_node('a decision node',(0.5,0.1),(0.1,0.5),decision_on_node)
	plot_node('a leaf node',(0.8,0.1),(0.3,0.8),leaf_node)
	plt.show()

#---------------------------------------------------------
def get_num_leaves(my_tree):
	num_leaves = 0
	list_keys = list(my_tree.keys())
	first_str = list_keys[0]
	second_dict = my_tree[first_str]
	for key in second_dict.keys():
		if type(second_dict[key]).__name__=='dict':
			num_leaves += get_num_leaves(second_dict[key])
		else:
			num_leaves +=1
	return num_leaves

def get_tree_depth(my_tree):
	max_depth = 0
	list_keys = list(my_tree.keys())
	first_str = list_keys[0]
	second_dict = my_tree[first_str]
	for key in second_dict.keys():
		if type(second_dict[key]).__name__=='dict':
			this_depth = 1 + get_tree_depth(second_dict[key])
		else:
			this_depth = 1
		if this_depth > max_depth: max_depth = this_depth
	return max_depth

#-----------------------------------------------------------
def retrieve_tree(i):
	list_of_trees = [
	{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
	{'no surfacing': {0: 'no', 1: {'flippers': {0: {'head':{0: 'no', 1: 'yes'}}, 1:'no'}}}}]

	return list_of_trees[i]

