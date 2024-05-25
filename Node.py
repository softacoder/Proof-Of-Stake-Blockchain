from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from Message import Message

class Node():

    def __init__(self, ip, port, key=None):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()
        if key is not None:
            self.wallet.fromKey(key)    

    def startP2P(self):
        self.p2p = SocketCommunication(self.ip, self.port)
        self.p2p.startSocketCommunication(self)

    def startAPI(self):
        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start(apiPort)

    def handleTransaction(self, transaction):
        data = transaction.payload()
        signature = transaction.signature()
        signerPublicKey = transaction.senderPublicKey
        signatureValid = Wallet.signatureValid(data, signature, signerPublicKey)
        transactionExists = self.transactionPool.transactionExists(transaction)
        transactionInBlock = self.blockchain.transactionExists(transaction)
        if not transactionExists and not transactionInBlock and signatureValid:
            self.transactionPool.addTransaction(transaction)
            message = Message(self.p2p.socketConnector, 'TRANSACTION', transaction)
            encodedMessage = BlockchainUtils.encode(message)
            self.p2p.broadcast(encodedMessage)
            forgingRequired = self.transactionPool.forgerRequired()
            if forgingRequired:
                self.forge()

        def handleBlock(self, block):
            forger = block.forger
            blockHash = block.payload()
            signature = block.signature

            blockCountValid =self.blockchain.blockCountValid(block)
            lasBlockHashValid = self.blockchain.lastBlockHashValid(block)
            forgerValid = self.blockchain.forgerValid(block)
            transactionValid = self.blockchain.transactionValid(
                block.transactions)
            signatureValid = Wallet.signatureValid(blockHash, signature, forger)
            if lastBlockHashValid and forgerValid and transactionValid and signatureValid and blockCountValid:
                self.blockchain.addBlock(block)
                self.transactionPool.removeFromPool(block.transactions)
                message = Message(self.p2p.socketConnector, 'BLOCK', block)
                encodeMessage = BlockchainUtils.encode(message)
                self.p2p.broadcast(encodeMessage)

        def forge():
            forger = self.blockchain.nextForger()
            if forger == self.wallet.publicKeyString():
                print('i am the next forger')
                block = self.blockchain.createBlock(self.transactionPool.transactions, self.wallet)
                self.transactionPool.removeFromPool(block.transactions)
                message = Message(self.p2p.socketConnector, 'BLOCK', block)
                encodeMessage = BlockchainUtils.encode(message)
                self.p2p.broadcast(encodedMessage)
            else:
                print('i am not the next forger')
    