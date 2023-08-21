# nanoChatGpt

![nanoChatGPT](https://github.com/VatsaDev/nanoChatGPT/blob/fbe107f9687464a1bea9b052009389f92a96983f/assets/template.png)

a barebones Nanogpt, but finetuned on conversational data 

[Colab link](https://colab.research.google.com/drive/1a2aW5eClKjHVQJp-qtHDz4m6ai4yh49Z?usp=sharing)   
all updates in [updates.md](updates.md)
## how does it work?

This is a fork of Nanogpt, but trained on the data format of a chatbot like chatgpt, with the format inspired by `oasst-pythia-12b` 

```
<human> ... <endOfText>
<Bot> ... <endOfText>
<human> ... <endOfText>
<Bot> ... <endOfText>
<human> ... <endOfText>
<Bot> ... <endOfText>
```

The training data is a cleaned up, conversational version of the PersonaChat Dataset, compressed into a single `input.txt`. It is trained on the gpt-2-medium model, as that was the best colab could handle. 

## Demo
to view its capabilites, simply run the colab, the whole thing should take around ~5 minutes on a t4 instance. If you look at both outputs, you would notice the model definitly requires prompting, with the ideal prompting being

```
<human> ... <endOfText>
<Bot> ... <endOfText>
<Human> ... <endOfText>
<Bot>
```

## Limitations 

I did not make the data dumps/corpuses that make up this data, and can't account for any biases, as the dataset it self is based off the conversations of real people who may or may not have had biases. The model is meant for academic research purposes, and isn't meant for any important or high risk scenarios. Do not follow its advice

### whats in the data
 - personaChat corpus
 - twitter Dumps corpus
 - Ubuntu dialog corpus
 - Chatbot arena conversations (not for commercial use)
 - ParlAI empathetic Chat (not for commercial use)

for commercial purposes, just take the files `input1.txt` through `input36.txt`

## Features

 * Medium Dataset(270mb) and growing
 * Eariler the model would grow extremely repetitive after 15-30 tokens, now its pretty good at 150 or so tokens. It would also also start repeating the bot prompt or replace it with human names, but with recent increases in data, it happens very rarely.
 * The model used to not generate good anwsers, or proper english, and often have incomplete generations. Though with more data flowing in and the endOfText Token in Model Generation, we can check for incomplete sentences and get better responses.

## Problems / TODOs

* ### Very small conversations
    
    * Right now, the dataset used is made up of very small conversations, at best 8-10 sentences long, so including more medium-sized and large conversations is a necessity

* ### bigger models
     * try using huggingface methods, etc, to get up to gpt2-xl

* ### Add a stop function like the OpenAI API
    
    * Add the function to stop at a certain word, to allow for the model to stop, so the human can respond.

* ### Math and Logical Reasoning
    
    * While mostly out of the scope of this model, the two main options are to detect math and run backend code, or train the model with Chain-of-though math prompting, which is probably more feasible, For logical reasoning, I might try incorporating datasets like `garage-bAInd/Open-Platypus`, etc
    
* ### no memory/recall
    
    * With many models, you can ask what you were just talking about or to summarize the conversation above. When that is attempted with this model:
        
        ```plaintext
        Human: Dogecoin is cool 
        Bot: indeed, very shibe
        Human: what were we just talking about?
        Bot: me and a friend gave up on mining, but now I can
        ```
        
        as we can see, it continues on with a sentence on mining, confirming that it understood the context(GPT2 info) but it does not have the ability to recall. I suspect that has to do with the models data, and that if I were to feed it data like short-context calling and summarization data, it would gain those abilities

      
<br /><br /><br />
Anyone Who can contribute to the repo, please do so, any and all contributions are welcome, simply add a little to `input.txt` and expand our dataset would be amazing.

#### citations
```
@misc{zheng2023judging,
      title={Judging LLM-as-a-judge with MT-Bench and Chatbot Arena}, 
      author={Lianmin Zheng and Wei-Lin Chiang and Ying Sheng and Siyuan Zhuang and Zhanghao Wu and Yonghao Zhuang and Zi Lin and Zhuohan Li and Dacheng Li and Eric. P Xing and Hao Zhang and Joseph E. Gonzalez and Ion Stoica},
      year={2023},
      eprint={2306.05685},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
