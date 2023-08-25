import os
import requests
import tiktoken
import numpy as np

# download concatenated.txt file from huggingface
def download_file(url):
  response = requests.get(url)
  if response.status_code == 200:
    with open('dataset.txt', 'wb') as f:
      f.write(response.content)
  else:
    print('Error downloading file:', response.status_code)

download_file('https://huggingface.co/VatsaDev/ChatGpt-nano/resolve/main/Dataset.txt')

# get input file
input_file_path = './dataset.txt';

with open(input_file_path, 'r') as f:
    data = f.read()

# define train and val sizes
train_size = 0.9
val_size = 0.1

# split data into train and val sets
train_data = data[:int(len(data)*train_size)]
val_data = data[int(len(data)*train_size):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")

# encode train chunks
train_ids = enc.encode_ordinary(train_data)

# encode val chunks
val_ids = enc.encode_ordinary(val_data)

# export train and val chunks to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))

val_ids = np.array(val_ids, dtype=np.uint16)
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")
