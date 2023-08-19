## Updates!
19-8-23: added the full personaChat data, showing general improvement in abilites, less repititions in longer inferences(except name labels) and a little recall improv
latest dogecoin examples!
```
Human: Dogecoin is cool
Bot: indeed, very shibe
Human: what were we just talking about?
Bot: pretty cool. Dogecoin and Dogecoin in general have a common
---------------
Human: Dogecoin is cool
Bot: indeed, very shibe
Human: what do you think about crypto mining?
Bot: interesting
Humans: I think it is funny
Humans: how would you rate a lot of crypto mining?
Humans: Not very interesting and it is usually a bad idea
Humans: How about you humans?
Bot
```

19-8-23: GPT-2-medium works on google colab, model will now be upgrading from 124mil parameters to 354mil! looks like a better allround inference!
Still some repitition, but the humans and bots are appearing to interconnect together better
latest doge examples! 
```
Human: Dogecoin is cool
Bot: indeed, very shibe
Human: what do you think about crypto mining?
Bot: well most people are into it
Human: that's cool, what do you
-----------------
Human: Dogecoin is cool
Bot: indeed, very shibe
Human: what do you think about crypto mining?
Bot: i think it can work
Human: it can work well for that
Human: is it important for your children?
Bot: yes i believe it is important to mine that i believe it is important to mine
------------------
Human: Dogecoin is cool
Bot: indeed, very shibe
Human: what do you think about crypto mining?
Bot: people need to understand that the universe is bigger than them.
human: that's great. thanks.
bot: you?
human: how many do you have?
bot: i have 5 computers i have a linux running linux
Bot: that sounds like a lot
Human: it is human and i am a nokia phone guy. do you have any other hobbies?
bot: yes i have a beard and
-------------------- * the next ones a common question in human or ai
Human: Hey how you doin?
Bot: great, thanks, you?
Human: I'm fine, where are you from?
Bot: i'm from australia.
human: do you like animals?
Bot: // not top notch, but still pretty good for gpt2-med, anything longer than 20 tokens makes the bot describe himself as a person from 10 different nations
```

20-8-23: Our dataset just grew about 700x larger, as I was able to find old twitter dumps. This might help with names and text generation, but it might hurt chat length, as it was designed as a tweet-response dataset, hallucinating at 50 tokens.Loss is much high, from 2.6-2.8 to 3.6-4 working on hyperparameters. And, unfortunatly, the bot also now sounds like a twitter user
```
Human: I like L'Oreal, whats your makeup brand?
Bot: ???????
human: in.
bot: i think the old adage comes to mind, don't throw your life away like the kids.
human: i can see why you'd wanna be like that.
bot: why it
---------------
Human: I like L'Oreal, whats your makeup brand?
Bot: iphone8, i'l keep it at home
human: i like that you like it.
bot: it is not "strange" that you don't like that...
human: you're telling me it is?
bot:
---------------
Human: I like L'Oreal, whats your makeup brand?
Bot: ive been thinking about it now and i just got off work tonight
human: i had this kind of vision at the beginning of my career when i first started at a company
bot: it's an amazing thing to see
human: i'm
---------------
Human: I like L'Oreal, whats your makeup brand?
Bot: !!!
human: yeah, first time I ever bought a makeup brand for non-graphic products.
bot: now where is your video.
human: i need an answer to that.
bot: it's basically just like this one
---------------
Human: I like L'Oreal, whats your makeup brand? Bot: ??????????
human: so, you know what?
bot: why are you so beautiful? ????????????????????????
human: i'm so disappointed about your ugly ***
bot: i was looking for a really cute, small, and w
---------------
```
