class Tree_node:
    def __init__(self,name_value,num_occur, parent_node):
        self.name = name_value
        self.count = num_occur
        self.node_link = None
        self.parent = parent_node
        self.children = {}

    def inc(self,num_occur):
        self.count+= num_occur

    def disp(self,ind=1):
        print(" "*ind, self.name,"  ", self.count)
        for child in self.children.values():
            child.disp(ind+1)

def create_tree(data_set,min_support = 1):
    header_table = {}
    for trans in data_set:
        for item in trans:
            header_table[item] = header_table.get(item,0) + data_set[trans]
    for k in header_table:
        if header_table[k] < min_support:
            del(header_table[k])
    freq_item_set = set(header_table.keys())
    if len(freq_item_set) == 0: return None,None
    for k in header_table:
        header_table[k] = [header_table[k],None]
    ret_tree = Tree_node('Null set',1,None)
    for trans_set,count in data_set.iteritems():
        localD={}
        for item in trans_set:
            if item in freq_item_set:
                localD[item]=header_table[item][0]
        if len(localD)>0:
            ordered_items = [v[0] for v in sorted(localD.items(),key = lambda p: p[1],reverse = True)]
            update_tree(ordered_items,ret_tree,header_table,count)
    return ret_tree,header_table

def update_tree(items,in_tree,header_table,count):
    if items[0] in in_tree.children:
        in_tree.children[items[0]].inc(count)
    else:
        in_tree.children[items[0]] = Tree_node(items[0],count,in_tree)
        if header_table[items[0]][1] == None:
            header_table[items[0]][1] = in_tree.children[items[0]]
        else:
            update_header(header_table[items[0]][1],in_tree.children[items[0]])
    if len(items) >1:
        update_tree(items[1::],in_tree.children[items[0]],header_table,count)

def update_header(node_to_test,target_node):
    while (node_to_test.node_link != None):
        node_to_test = node_to_test.node_link
    node_to_test.node_link = target_node

def ascend_tree(leaf_node,prefix_path):
    if leaf_node.parent != None:
        prefix_path.append(leaf_node.name)
        ascend_tree(leaf_node.parent,prefix_path)

def find_prefix_path(base_path,tree_node):
    cond_paths = {}
    while tree_node != None:
        prefix_path = []
        ascend_tree(tree_node,prefix_path)
        if len(prefix_path)>1:
            cond_paths[frozenset(prefix_path[1:])]=tree_node.count
        tree_node = tree_node.node_link
    return cond_paths
def mine_tree(in_tree, header_table,min_sup)

