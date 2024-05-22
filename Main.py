from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block

if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    fraudulentWallet = Wallet()
    pool = TransactionPool()

    transaction = wallet.createTransaction(receiver, amount, type)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    if pool.transactionExists(transaction) == False:
        pool.addTransaction(transaction)

    block = Block(pool.transactions, 'lastHash', 'forger', 1)

    print(block.toJson())
