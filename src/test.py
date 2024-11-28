import base58
# Base58 解码
decoded = base58.b58decode("g7NkLW3SMdjWG")
print(f"解码后的数据: {decoded}")  # 输出原始字节数据
instruction = decoded[0:1]
data = decoded[0:]
encoded = base58.b58encode(instruction)
print(f"解码后的数据: {instruction}")  # 输出原始字节数据
encoded = base58.b58encode(data)
print(f"解码后的数据: {data}")  # 输出原始字节数据