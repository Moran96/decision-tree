import matplotlib.pyplot as plt

decision_on_node = dict(boxstyle="sawtooth", fc="0.8")
leaf_node = dict(boxstyle="round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")

#draw the node
def plot_node(node_txt,center_pt,parent_pt,node_type):
	create_plot.ax1.annotate(node_txt,xy=parent_pt,xycoords='axes fraction',
		xytext=center_pt,textcoords='axes fraction',
		va="center",ha="center",bbox=node_type,arrowprops=arrow_args)

#make text information between node_father and node_son.
def plot_mid_text(center_pt,parent_pt,txt_string):
	x_mid = (parent_pt[0]-center_pt[0])/2.0 + center_pt[0]
	y_mid = (parent_pt[1]-center_pt[1])/2.0 + center_pt[1]
	create_plot.ax1.text(x_mid,y_mid,txt_string)

#calculate the width and height
def plot_tree(my_tree,parent_pt,node_txt):
	num_leaves = get_num_leaves(my_tree)
	depth = get_tree_depth(my_tree)
	list_keys = list(my_tree.keys())
	first_str = list_keys[0]
	center_pt = (plot_tree.xOff + (1.0 + float(num_leaves))/2.0/plot_tree.totalW,\
		plot_tree.yOff)
	plot_mid_text(center_pt,parent_pt,node_txt)
	plot_node(first_str,center_pt,parent_pt,decision_on_node)
	second_dict = my_tree[first_str]
	plot_tree.yOff = plot_tree.yOff - 1.0/plot_tree.totalD
	for key in second_dict.keys():
		if type(second_dict[key]).__name__=='dict':
			plot_tree(second_dict[key],center_pt,str(key))
		else:
			plot_tree.xOff = plot_tree.xOff + 1.0/plot_tree.totalW
			plot_node(second_dict[key],(plot_tree.xOff,plot_tree.yOff),
				center_pt,leaf_node)
			plot_mid_text((plot_tree.xOff,plot_tree.yOff),center_pt,str(key))
	plot_tree.yOff = plot_tree.yOff + 1.0/plot_tree.totalD

#draw the tree in matplotlib. 
def create_plot(in_tree):
	fig = plt.figure(1,facecolor='white')
	fig.clf()

	axprops = dict(xticks=[],yticks=[])
	create_plot.ax1 = plt.subplot(111,frameon=False, **axprops)

	plot_tree.totalW = float(get_num_leaves(in_tree))
	plot_tree.totalD = float(get_tree_depth(in_tree))
	plot_tree.xOff = -0.5/plot_tree.totalW; plot_tree.yOff = 1.0;
	plot_tree(in_tree,(0.5,1.0),'')
	
	# plot_node('a decision node',(0.5,0.1),(0.1,0.5),decision_on_node)
	# plot_node('a leaf node',(0.8,0.1),(0.3,0.8),leaf_node)
	plt.show()

#get the number of a tree.
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

#get the depth of a tree.
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

#create a series of trees in a list.
def retrieve_tree(i):
	list_of_trees = [
	{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
	{'no surfacing': {0: 'no', 1: {'flippers': {0: {'head':{0: 'no', 1: 'yes'}}, 1:'no'}}}}]

	return list_of_trees[i]

