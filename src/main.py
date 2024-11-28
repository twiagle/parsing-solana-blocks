import sys
# sys.path.append()

import json
from src.parser.transaction_parser import parse_transaction_from_block
from src.parser.instruction_parser import parse_instruction_from_block

if __name__ == "__main__":
    txs = []
    instructions = []
    with open('29867972-29868122.blocks', 'r', encoding='utf-8') as file:
        for line in file:
            line = file.readline().strip()
            if line:
                block = json.loads(line)
                txs = parse_transaction_from_block(block, "sonic_testnet")
                instructions = parse_instruction_from_block(block, "sonic_testnet")
    with open("parsed_transactions_testnet_29867972-29868122.json", "w") as f:
        json.dump(txs, f, indent=2)
    with open("parsed_instructions_testnet_29867972-29868122.json", "w") as f:
        json.dump(instructions, f, indent=2)
    # spl token
    with open('343156956.json', 'r', encoding='utf-8') as file:
        block = json.load(file).get("result")
        txs = parse_transaction_from_block(block, "sonic_testnet")
        instructions = parse_instruction_from_block(block, "sonic_testnet")
    with open("parsed_transactions_testnet_343156956.json", "w") as f:
        json.dump(txs, f, indent=2)
    with open("parsed_instructions_testnet_343156956.json", "w") as f:
        json.dump(instructions, f, indent=2)
    # sol native
    with open('343158827.json', 'r', encoding='utf-8') as file:
        block = json.load(file).get("result")
        txs = parse_transaction_from_block(block, "sonic_testnet")
        instructions = parse_instruction_from_block(block, "sonic_testnet")
    with open("parsed_transactions_testnet_343158827.json", "w") as f:
        json.dump(txs, f, indent=2)
    with open("parsed_instructions_testnet_343158827.json", "w") as f:
        json.dump(instructions, f, indent=2)
    # OpenMysteryBox
    with open('5941200.json', 'r', encoding='utf-8') as file:
        block = json.load(file).get("result")
        txs = parse_transaction_from_block(block, "sonic_testnet")
        instructions = parse_instruction_from_block(block, "sonic_testnet")
    with open("parsed_transactions_testnet_5941200.json", "w") as f:
        json.dump(txs, f, indent=2)
    with open("parsed_instructions_testnet_5941200.json", "w") as f:
        json.dump(instructions, f, indent=2)
