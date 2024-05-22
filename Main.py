from Transaction import Transaction
from Wallet import Wallet

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    transaction = Transaction(sender, receiver, amount, type)
   
    wallet = Wallet()
    signature = wallet.sign(transaction.toJson())
    
    # transaction.sign(signature)
    
    signatureValid = Wallet.signatureValid(
        transaction.toJson(), wallet.publicKeyString())

print(signatureValid)
