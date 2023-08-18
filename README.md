# nanoChatGpt

Nanogpt, but finetuned on conversational data 

[Colab link](https://colab.research.google.com/drive/1a2aW5eClKjHVQJp-qtHDz4m6ai4yh49Z?usp=sharing)

This is a fork of Nanogpt, but trained on the data format of a chatbot like chatgpt, with the format inspired by `redpajama-chat`

```
Human: ...
Bot: ...
Human: ...
Bot: ...
Human: ...
Bot: ...
```

The training data is a cleaned up, conversational version of the PersonaChat Dataset, compressed into a single `input.txt` I only converted about a thousand lines of conversation, and then copy-pasted 40 times to have a sizeable dataset. it is trained on the regular 124mil param gpt-2, as that was the best colab could handle. 

## Demo
to view its capabilites, simply run the colab, the whole thing should take around ~5 minutes on a t4 instance. If you look at both outputs, you would notice the model definitly requires prompting, with the ideal prompting being

```
Human: ...
Bot: ...
Human: ...
Bot:
```

## Limitations 

I did not make the database, and can't account for any biases, as the dataset it self is based off the conversations of real people who may or may not have had biases. The model is meant for academic research purposes, and isn't meant for any important or high risk scenarios. Do not follow its advice

## Problems / TODOs
 - ### Very small dataset
    - Right now, the dataset is a very small right now, the current data was just copy-paste conversions, and definitly needs to be automated 
 - ### Very small conversations
    - Right now, the dataset used is made up of very small conversations, at best 8-10 sentences long, so including more medium sized and large conversations is a necessity
 - ### Repetitive with larger amounts of tokens
    - While this effect is greatly reduced with prompting, it turns extremely repetitive when asked for more than 15-30 tokens. It can also start repeating the bot prompt or replace it with human names

example:
```
Human: Hi, how are you? Bot: i'm good, how are you? Human: I'm good: where are you from? Bot: i live in seattle, seattle, seattle, seattle

Bot: Hi, how are you? Bot: i'm good, how are you? Human: i live in seattle, seattle, seattle, seattle, seattle

Bot: Hi, how are you? Bot: i'm good, how are you? Human: i live in seattle, seattle, seattle, seattle, seattle

Bot: Yo,
```
- ### Not having clear anwser and also continuing to generate an anwser 
    - While this effect is greatly reduced with more and better data, the model probably needs padding to set outputs to a certain size, and also probably a stop at a certain word function.
 - ### no memory/recallation
    - With many models, you can ask what you were just talking about or to summarize the conversation above. When that is attempted with this model:
      ``` 
      Human: Dogecoin is cool 
      Bot: indeed, very shibe
      Human: what were we just talking about?
      Bot: me and a friend gave up on mining, but now I can
      ```
      as we can see, it continues on with a sentence on mining, confirming that it understood the context(GPT2 info) but it does not have the ability to recall. I suspect that has to do with the models data, and that if I were to feed it data like short-context calling and summarization data, it would gain those abilities 


Anyone Who can contribute to the repo, please do so, any and all contributions are welcome, simply add a little to `input.txt` and expand our dataset would be amazing.
