from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
import pprint
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

if __name__ == '__main__':
   
    blockchain = Blockchain()
    pool = TransactionPool()

    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()

    exchangeTransaction = exchange.createTransaction(
        alice.publicKeyString(), 10, 'EXCHANGE')
    
    if not pool.transactionExists(exchangeTransaction):
        pool.addTransaction(exchangeTransaction)

    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    blockOne = Block(coveredTransaction, lastHash, forger.publicKeyString(), blockCount)
    blockchain.addBlock(blockOne)

    #alice wants to spend 5 tokens to bob
    transaction = alice.createTransaction(bob.publicKeySTring(), 5, 'TRANSFER')

    if not pool.transactionExists(transaction):
        pool.addTransaction(transaction)

    coveredTransaction = blockchain.getCoveredTransactionSet(pool.transactions)
    lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    blockCount = blockchain.blocks[-1].blockCount + 1
    blockTwo = Block(coveredTransaction, lastHash, forger.publicKeyString(), blockCount)
    blockchain.addBlock(blockTwo)

    pprint.pprint(blockchain.toJson())