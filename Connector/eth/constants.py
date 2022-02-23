#!/usr/bin/python3
GET_BALANCE_METHOD = "eth_getBalance"
GET_BLOCK_BY_NUMBER_METHOD = "eth_getBlockByNumber"
GET_BLOCK_BY_HASH_METHOD = "eth_getBlockByHash"
GET_TRANSACTION_BY_HASH_METHOD = "eth_getTransactionByHash"
GET_TRANSACTION_COUNT_METHOD = "eth_getTransactionCount"
GET_GAS_PRICE_METHOD = "eth_gasPrice"
GET_TRANSACTION_RECEIPT_METHOD = "eth_getTransactionReceipt"
SEND_RAW_TRANSACTION_METHOD = "eth_sendRawTransaction"
ESTIMATE_GAS_METHOD = "eth_estimateGas"
SUBSCRIBE_METHOD = "eth_subscribe"
SYNCING_METHOD = "eth_syncing"
CALL_METHOD = "eth_call"

NEW_HEADS_SUBSCRIPTION = "newHeads"

RPC_JSON_SCHEMA_FOLDER = "eth/rpcschemas/"
WS_JSON_SCHEMA_FOLDER = "eth/wsschemas/"
SCHEMA_CHAR_SEPARATOR = "_"
REQUEST = "request"
RESPONSE = "response"
SCHEMA_EXTENSION = ".json"

GET_ADDRESS_BALANCE = "getaddressbalance"
GET_ADDRESSES_BALANCE = "getaddressesbalance"
GET_HEIGHT = "getheight"
BROADCAST_TRANSACTION = "broadcasttransaction"
GET_BLOCK_BY_HASH = "getblockbyhash"
GET_BLOCK_BY_NUMBER = "getblockbynumber"
GET_ADDRESS_TRANSACTION_COUNT = "getaddresstransactioncount"
GET_ADDRESSES_TRANSACTION_COUNT = "getaddressestransactioncount"
GET_GAS_PRICE = "getgasprice"
ESTIMATE_GAS = "estimategas"
GET_TRANSACTION = "gettransaction"
GET_TRANSACTION_RECEIPT = "gettransactionreceipt"
SUBSCRIBE_ADDRESS_BALANCE = "subscribetoaddressbalance"
UNSUBSCRIBE_ADDRESS_BALANCE = "unsubscribefromaddressbalance"
SYNCING = "syncing"
CALL = "call"
SUBSCRIBE_TO_NEW_BLOCKS = "subscribetonewblocks"
UNSUBSCRIBE_FROM_NEW_BLOCKS = "unsubscribefromnewblocks"

COIN_SYMBOL = "eth"
DEFAULT_PKG_CONF = "defaultConf.json"


"""
CONFIRMED = "confirmed"
UNCONFIRMED = "unconfirmed"
PENDING = "pending"
LATEST = "latest"
ADDRESS = "address"
ADDRESSES = "addresses"
LATEST_BLOCK_INDEX = "latestBlockIndex"
NUMBER = "number"
LATEST_BLOCK_HASH = "latestBlockHash"
HASH = "hash"
BROADCASTED = "broadcasted"
FROM = "from"
AMOUNT = "amount"
VALUE = "value"
TRANSACTION = "transaction"
TRANSACTIONS = "transactions"
INPUTS = "inputs"
OUTPUTS = "outputs"
TRANSACTION_COUNT = "transactionCount"
GAS_PRICE = "gasPrice"
ESTIMATED_GAS = "estimatedGas"
BALANCE = "balance"
TO = "to"
RAW_TRANSACTION = "rawTransaction"
TX_HASH = "txHash"
BLOCK_HASH = "blockHash"
BLOCK_NUMBER = "blockNumber"
TX = "tx"
INCLUDE_TRANSACTIONS = "includeTransactions"
CURRENT_BLOCK_INDEX = "currentBlockIndex"
CURRENT_BLOCK = "currentBlock"
HIGHEST_BLOCK = "highestBlock"
SYNC_PERCENTAGE = "syncPercentage"
"""
