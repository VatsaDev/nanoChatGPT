import os
import requests
import tiktoken
import numpy as np

import os
import requests
import glob

#concatenates all inputs
def concatenate_text_files(file_paths):
  with open("concatenated.txt", "w") as outfile:
    for file_path in file_paths:
      response = requests.get(file_path)
      text = response.text
      outfile.write(text)

  return os.path.abspath("concatenated.txt")

#save file in colab
file_paths = ["https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input1.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input2.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input3.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input4.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input5.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input6.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input7.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input8.txt"]
concatenated_file_path = concatenate_text_files(file_paths)

print(f"The concatenated file is saved at {concatenated_file_path}.")

# get input file
input_file_path = os.path.join(os.path.dirname(__file__), 'input.txt')
if not os.path.exists(input_file_path):
    data_url = '/content/nanoChatGPT/concatenated.txt';
    with open(input_file_path, 'w') as f:
        f.write(requests.get(data_url).text)

with open(input_file_path, 'r') as f:
    data = f.read()
n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))

