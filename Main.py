from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
import sys


if __name__ == '__main__':

   ip = sys.argv[1]
   port = (sys.argv[2])
   apiPort = int(sys.argv[3])
   keyFile = None
   if len(sys.argv) > 4:
      keyFile = sys.argv[4]

   node = Node(ip, port)
   node.startP2P()
   node.startAPI(apiPort)

   
   