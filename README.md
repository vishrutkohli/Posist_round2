# Posist_round2 Assesment

The project develops a Dynamic list of unordered records. 

### Prerequisites

You will need python2.7 to run this program. 
And install an external cryptographic library to encode and decode the strings.

pip install pycrypto (By running the following command)

**Documentation**

The library contains two modules 
1.) ***NodeData*** 
*This contains all the functions which will work on the data. 
functions:*
- Encryption of key(Task 4)
- Decryption of key(Task 4)
- Ownership changing(Task 7)
- Get data (internal function)
- Edit Value(Task 6)
- Verify owner(5)
- Get owner name(internal function)
- Get owner id(internal function)
- Get value(internal function)
                     
2.) ***CustomTree***  - This contains all the functions which will work on the Treechain. 
Functions:
**Class TreeNode**
- is Valid Node(internal Function)
- add Node(Task 3)
- transfer Owner(Task 7)
- edit Node(Task 6)
- edit Value(Task 6)                     

**Class TreeChain:**
- Get longest chain(Task 8 and9)               
                     
## Screenshot
![alt text](https://i.imgur.com/SiFF8FE.png)
## Deployment
- As of now this is just a simple python app/module but can be easily converted to a scalable backend using Django 

## Additional Features
- **We also have support to search the node beloging to a particular owner and perform operations on it.**

## Author

Vishrut Kohli


