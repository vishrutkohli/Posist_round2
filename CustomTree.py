import uuid
from datetime import datetime
import hashlib
from NodeDataClass import NodeData

## Creating a class for the tree node 
class Treenode:
	def __init__(self,tree_chain,owner_name,value,parent_node,genesis_node,node_num):
		print "Creating a tree node for owner : ",owner_name
		self.time_stamp=str(datetime.now())
		self.node_id=uuid.uuid4().hex
		self.data=NodeData(value,owner_name,self.node_id)
		self.parent_id=parent_node
		self.node_num=node_num
		self.child_list=[]
		self.genesis_node_id=genesis_node
		self.hash=hashlib.sha512(b''+str(self.time_stamp)+str(owner_name)+str(self.node_id)+str(self.data.get_data)+str(self.parent_id)+str(self.genesis_node_id))
		self.value_carryover=value
		self.tree_chain=tree_chain

	def isValidNode(self,Node):
		# print Node.data.get_value()
		# print self.value_carryover
		if int(Node.data.get_value())>int(self.value_carryover):
			return False
		else:
			print "this"
			return True

	def addNode(self,Node):
		print("Adding a new node......")
		if(self.isValidNode(Node)):
			self.child_list.append(Node)
			self.value_carryover=self.value_carryover-int(Node.data.get_value())
			self.tree_chain.owner_map[Node.data.get_owner_name]=Node
			self.tree_chain.node_map[Node.node_id]=Node
			print "New Node Added for "+Node.data.get_owner_name()+" under the parent "+self.data.get_owner_name()
		else:
			print("The node is invalid")

	def transferOwner(self,n_owner_name):
		print("Transferring Ownership from ",self.owner_name," to  ",n_owner_name)
		self.data.change_ownership(n_owner_name,self.owner_name,self.node_id)

	def edit_node(self,new_val):
		pass

class TreeChain:
	def __init__(self):
		self.genesis_node=None
		self.node_map={}
		self.owner_map={}
	
	def setGenesisNode(self,genesis_node):
		self.genesis_node=genesis_node
		self.owner_map[genesis_node.data.get_owner_name()]=genesis_node
		self.node_map[genesis_node.node_id]=genesis_node

	def getLongestChain(self,node):
		if(len(node.child_list)==0):
			return 1
		else:
			max_num=-1;
			for i in node.child_list:
				count=self.getLongestChain(i)
				if(count>max_num):
					max_num=count
			return max_num+1;


## Some Pilot Code 
tree_chain=TreeChain()
genesis_node=Treenode(tree_chain,"Posist",10,"NULL","NULL",0)
tree_chain.setGenesisNode(genesis_node)
tree_chain=TreeChain()
print("Generating Genesis Node.....")
genesis_node=Treenode(tree_chain,"Posist",10,"NULL","NULL",0)
tree_chain.setGenesisNode(genesis_node)

## create a new node of the genesis node
b=Treenode(tree_chain,"Vishrut Kohli",9,genesis_node.node_id,genesis_node.node_id,0)
genesis_node.addNode(b);
c=Treenode(tree_chain,"Nipun Arora",8,genesis_node.node_id,genesis_node.node_id,0)
b.addNode(c)
d=Treenode(tree_chain,"Shivam Kohli",7,genesis_node.node_id,genesis_node.node_id,0)
c.addNode(d)
print "The length for the longest chain at genesis node is :"
print tree_chain.getLongestChain(genesis_node)

