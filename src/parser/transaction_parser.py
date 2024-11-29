from typing import Dict, List, Text
from datetime import datetime

def parse_transaction_from_block(block, source="sonic_testnet"):
  responses = []
  transactions = block.get("transactions")
  
  for idx, tx in enumerate(transactions):
    signatures = tx.get("transaction").get("signatures")
    meta = tx.get("meta", {})
    response = {}
    response["hash"] = signatures[0] if signatures else ""
    response["nonce"] = None
    response["transaction_index"] = idx
    # response["from_address"] =
    # response["to_address"] =
    # response["value"] = 
    response["gas"] = meta.get("fee", 0)
    response["gas_price"] = 1 # Solana uses different fee model
    # response["input"] = tx.get("transaction").get("message").get("instructions")
    response["receipt_cumulative_gas_used"] = meta.get("fee", 0)
    response["receipt_gas_used"] = meta.get("fee", 0)
    response["receipt_contract_address"] = None
    response["receipt_root"] = None
    response["receipt_status"] = 1 if meta.get("err", None) else 0 # no error = 0, with error = 1
    response["block_timestamp"] = block.get("blockTime", 0)
    response["block_number"] = block.get("blockHeight", 0)
    response["block_hash"] = block.get("blockHash")
    response["max_fee_per_gas"] = 0
    response["max_priority_fee_per_gas"] = 0
    response["response_type"] = 0
    response["receipt_effective_gas_price"] = 0
    response["source"] = source
    response["created_at"] = datetime.now().isoformat()
    responses.append(response)
  return responses