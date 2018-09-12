import uuid
from datetime import datetime
import hashlib
from NodeDataClass import NodeData

## Creating a class for the tree node 
class Treenode:
	def __init__(self,tree_chain,owner_name,value,parent_node,genesis_node,node_num):
		print("Creating a tree node for owner : ",owner_name)
		self.time_stamp=str(datetime.now())
		self.node_id=uuid.uuid4().hex
		self.data=NodeData(self.time_stamp,self.owner_name,self.owner_id)
		self.parent_id=parent_node
		self.node_num=node_num
		self.child_list=[]
		self.genesis_node_id=genesis_node
		self.hash=hashlib.sha512(b''+str(self.time_stamp)+str(owner_name)+str(self.node_id)+str(self.data.getString)+str(self.parent_id)+str(self.genesis_node_id))
		self.value_carryover=value
		self.tree_chain=tree_chain

	def isValidNode(self,Node):
		if Node.data.getValue()>self.value_carryover:
			return False
		else:
			return True

	def addNode(self,Node):
		print("Adding a new node......")
		if(isValidNode(Node)):
			self.child_list.append(Node)
			self.value_carryover=self.value_carryover-Node.data.getValue()
			self.tree_chain.owner_map[Node.data.getOwnerName]=Node
			self.tree_chain.node_map[Node.node_id]=Node
		else:
			print("The node is invalid")

	def transferOwner(self,n_owner_name):
		print("Transferring Ownership from ",self.owner_name," to  ",n_owner_name)
		self.data.change_ownership(n_owner_name,self.owner_name,self.node_id)

	def edit_node(self,new_val):
		pass

class TreeChain:
	def __init__(self,genesis_node):
		self.genesis_node=genesis_node
		self.node_map={}
		self.owner_map={}
		self.owner_map[genesis_node.data.getOwnerName()]=genesis_node
		self.node_map[genesis_node_id]=genesis_node

	def getLongestChain(self,node):
		if(len(node.child_list)==0):
			return 1
		else:
			max_num=-1;
			for i in node.child_list:
				count=self.dfsUtil(i)
				if(count>max_num):
					max_num=count
			return max_num+1;







