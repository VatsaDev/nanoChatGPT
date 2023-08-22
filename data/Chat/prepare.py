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
file_paths = ["https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input1.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input2.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input3.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input4.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input5.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input6.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input7.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input8.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input9.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input10.txt"
             "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input11.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input12.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input13.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input14.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input15.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input16.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input17.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input18.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input19.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input20.txt"
             "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input21.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input22.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input23.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input24.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input25.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input26.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input27.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input28.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input29.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input30.txt"
             "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input31.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input32.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input33.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input34.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input35.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input36.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input37.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input38.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input39.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input40.txt",
             "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input41.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input42.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input43.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input44.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input45.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input46.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input47.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input48.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input49.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input50.txt",
             "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input51.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input52.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input53.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input54.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input55.txt", "https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input56.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input57.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input58.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input59.txt","https://raw.githubusercontent.com/VatsaDev/nanoChatGPT/main/data/Chat/input60.txt"]
concatenated_file_path = concatenate_text_files(file_paths)

print(f"The concatenated file is saved at {concatenated_file_path}.")

# get input file
input_file_path = './concatenated.txt';
if not os.path.exists(input_file_path):
    data_url = 'https://www.dropbox.com/scl/fi/zsk7h4gg1pbzt02vwa4xh/concatenated.txt';
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

