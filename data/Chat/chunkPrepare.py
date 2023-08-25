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

# define chunk size
chunk_size = 512

def chunk_data(data, chunk_size):
  global chunks
  chunks = []
  for i in range(0, len(data), chunk_size):
    chunks.append(data[i:i+chunk_size])

  return chunks

# split data into train and val chunks
chunks = chunk_data(data, chunk_size)
num_chunks = len(chunks)
train_chunks = []
val_chunks = []
for i in range(0, num_chunks, 10):
  train_chunks.extend(chunks[i:i+9])

  # check the length of the chunks list before accessing the 9th element
  if i < num_chunks - 1:
    val_chunks.append(chunks[i+9])
  else:
    print("Not enough chunks to create val set")

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")

# encode train chunks
for chunk in train_chunks:
  train_ids = enc.encode_ordinary(chunk)

# encode val chunks
for chunk in val_chunks:
  val_ids = enc.encode_ordinary(chunk)

# export train and val chunks to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))

val_ids = np.array(val_ids, dtype=np.uint16)
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")
