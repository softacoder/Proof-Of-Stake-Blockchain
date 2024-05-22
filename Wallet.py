from Crypto.PublicKey import RSA
from Crypto.Signature import PKC51_v1_5
from BlockchainUtils import BlockchainUtils

class Wallet():

    def __init__(self):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        dataHash = BlockchainUtils.hash(data)
        signatureSchemeObject = PKC51_v1_5.new(self.keyPair)
        signature = signatureSchemeObject.sign(dataHash)
        return signature.hex()