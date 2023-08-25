import time

out_dir = '/content/drive/MyDrive/Model' # for google colab, for regular use, set value to 'out-chat'
eval_interval = 5
eval_iters = 50
wandb_log = False # feel free to turn on
wandb_project = 'gpt2finetune'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'Chat'
init_from = 'gpt2-medium' # this is the smallest GPT-2 model, good for google colab

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

batch_size = 4
gradient_accumulation_steps = 32
max_iters = 50

# finetune at constant LR
learning_rate = 2e-5
decay_lr = False
