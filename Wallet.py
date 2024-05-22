from Crypto.PublicKey import RSA
from Crypto.Signature import PKC51_v1_5
from BlockchainUtils import BlockchainUtils
from Transaction import Transaction         

class Wallet():

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKC51_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()
    
    @staticmethod 
    def signatureValid(data, signature, publicKeyString):
        signature = bytes.fromhex(signature)
        dataHash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemeObject = PKC51_v1_5.new()
        signatureValid = signatureSchemeObject.verify(dataHash, signature)
        return signatureValid
    
    def publicKeyString(self):
        publicKeyString = self.keyPair.getPublicKey().exportKey('PEM').decode('utf-8')
        return publicKeyString
    
    def createTransaction(self,receiver, amount, type):
        transaction = Transaction(
            self.publicKeyString(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        return transaction
