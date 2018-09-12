from Crypto.Cipher import AES
import base64

class NodeData:
	__secret_key = "posististhebest7"
	def __init__(self, value, owner_id , owner_name ):
		self.encrypted_string = self.encryption_of_key(value, owner_id , owner_name)
		
  
	def encryption_of_key(self , value, owner_id , owner_name):

		cipher = AES.new(NodeData.__secret_key,AES.MODE_ECB) 
		encoded = base64.b64encode(cipher.encrypt(str(owner_id) + "-" + str(owner_name) + "-"+str(value)))

		print "The value is encrypted"

		return encoded

	def change_ownership(self ,owner_id,value_new, owner_id_new , owner_name_new):
		verify_flag = verify_owner(owner_id)
		if(verify_flag == 1):
			self.encrypted_string = encryption_of_key(value_new, owner_id_new , owner_name_new )

			print "Ownership transfered to New user ID =" + owner_id_new

		else:
			print "Credentials of the users does not match"


	def decryption_of_key(self):
		cipher = AES.new(self.secret_key,AES.MODE_ECB) 
		decoded = cipher.decrypt(baes64.b64decode(self.encrypted_string))
		print " the value is decrypted"

		return decoded

	def get_data(self):

		return self.encrypted_string  

	def edit_value(self, owner_id, value_new):
		verify_flag = verify_owner(owner_id)

		if(verify_flag == 1):
			owner_name = get_owner_name()

			self.encrypted_string = encryption_of_key(value_new, owner_id , owner_name)

			print "The new value has been set"

		else:
			print "Credentials of the users does not match"


	def verify_owner(self , owner_id ):
		owner_id_orignal = self.get_owner_id()
		if(owner_id_orignal == owner_id):

			print "owner verified"
		else:
			print "Credentials of the users does not match"

		return 1    

	def get_owner_id(self):
		decrypted_key = decryption_of_key()
		splitted_key = decrypted_key.split('-')

		return splitted_key[0]

	def get_owner_name(self):
		decrypted_key = decryption_of_key()
		splitted_key = decrypted_key.split('-')

		return splitted_key[1]

	def get_value(self):
		decrypted_key = decryption_of_key()
		splitted_key = decrypted_key.split('-')

		return splitted_key[2]      


A = NodeData( 5 , "1234" , "vishrut")
		
		  