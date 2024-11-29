from pydoc import describe
from typing import Dict, Tuple, Text
import base58
import struct

def parse_event_type(program_id, instruction, account_keys, meta) -> Tuple[Text, Dict]:
    if program_id == "11111111111111111111111111111111":
        decoded = base58.b58decode(instruction.get("data"))
        cmd = decoded[0:4]
        if cmd == b'\x02\x00\x00\x00': 
            amount_little_endian = decoded[4:]
            amount = struct.unpack('<Q', amount_little_endian)[0] #u64
            return  "NativeSOLTransfer", {
                    "source": account_keys[instruction.get("accounts")[0]],
                    "destination": account_keys[instruction.get("accounts")[1]],
                    "lamports": amount,
            }
    elif program_id == "TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA": #  and instruction.get("data")[0:2] == "03"
        decoded = base58.b58decode(instruction.get("data"))
        cmd = decoded[0:1]
        if cmd == b'\x0c': 
            amount_little_endian = decoded[1:9]
            decimals_little_endian = decoded[9:10]
            amount = struct.unpack('<Q', amount_little_endian)[0] #u64
            decimals = struct.unpack('<B', decimals_little_endian)[0] #u8
            idx0 = instruction.get("accounts")[0]
            idx1 = instruction.get("accounts")[2]
            source = ""
            destination = ""
            for balance in meta.get("preTokenBalances"):
                if balance.get("accountIndex") == idx0:
                    source = balance.get("owner")
                elif balance.get("accountIndex") == idx1:
                    destination = balance.get("owner")
            return "SPLTokenTransferChecked",  {
                "token": meta.get("preTokenBalances")[0].get("mint"),
                "source": source,
                "destination": destination,
                "amount": amount,
                "decimals": decimals,
            }
    elif program_id in (
        "721v6F7kPhKoysprtn5d41k6vUYjbsGsQcB4D3Ac8Goc",
        "4MDghB3z9WY4NTy4gZQhH8rZ73ztWFhRPCX32zogohfu",
        "592fw8HNd6njPkNRjfbwG9qytTMvtjqEmDCT81GZGesQ",
        "FrFwm1G7uyapKegzPmaFknv38nUGMbomTiy2a2dvZx97",
        "CW6W21fRa6VRKYnVEyxyGp3vx6r5ov8dG2NxAYeGngFw",
        "7d1jRjkvgfZ55jTjfaTXeG8hoaHFuMnSsQi3QF5g9PcT",
    ):
        decoded = base58.b58decode(instruction.get("data"))
        cmd = decoded[0:8]
        if cmd == b'\xe1!\xc6\x01Z\x83>Z':  
            return "OpenMysteryBox",  {}
    return "UnknownInstruction", {} 

              
def parse_instruction_from_block(block, source="sonic_testnet"):
  responses = []
  transactions = block.get("transactions")
  for idx, tx in enumerate(transactions):
    meta = tx.get("meta", {})
    account_keys = tx.get("transaction").get("message").get("accountKeys")
    instructions = tx.get("transaction").get("message").get("instructions")
    signatures = tx.get("transaction").get("signatures")
    for idx, instruction in enumerate(instructions):
        response = {}
        programIdIndex = instruction.get("programIdIndex")
        response["blockId"] = block.get("blockHeight", 0)
        response["txId"] = signatures[0] if signatures else ""
        # response["signer"] = 
        response["programId"] = account_keys[programIdIndex]
        response["accounts"] = [account_keys[x] for x in instruction.get("accounts")]
        event_type, decoded_instruction = parse_event_type(response["programId"], instruction, account_keys, meta)
        response["eventType"] = event_type
        response["decodedInstruction"] = decoded_instruction
        responses.append(response)
  return responses