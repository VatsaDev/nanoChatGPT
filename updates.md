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
20-8-23: tuned hyperparameters, better in 15-20 tokens, gotten worse with 40+ tokens, tradeoff for a chatbot for simple turn conversations, and this effect will be offset by future data

Short:
```
Human: Hi, How are you doing?
Bot: good. You?
Human: !!!
bot: thanks i got a free ride?
human: no i need
---------------
Human: Hi, How are you doing?
Bot: good. You?
Human: ive been on a roll.
bot: my head is in a puddle
---------------
Human: Hi, How are you doing?
Bot: good. You?
Human: !!!
bot: good and i want to be together with you.
human:
---------------
Human: Hi, How are you doing?
Bot: good. You?
Human:  good.
Thanks for taking my call.
Bot: thanks! i'm
---------------
Human: Hi, How are you doing?
Bot: good. You?
Human: ive been in a lot of hospitals but not yet been through a lot of
---------------
```
Long(the twitter IQ really shows):
```
Human: Hi, How are you doing?
Bot: good. You?
Human: ive been here for a bit but it's been pretty much like a day in and day out.
bot: i have a pretty decent library. i just started reading them today.
human: i have a really good library of books i read all the
---------------
Human: Hi, How are you doing?
Bot: good. You?
Human: !!!!
Bot: !!!!
Human: yes! it is great. just telling you the story.
Bot: what story?
human: it is the story of our life.
bot: "i see your real face."
human: aww he did
---------------
Human: Hi, How are you doing?
Bot: good. You?
Human: !!!
bot: i have to take my headphones off to see someone and i'm just sitting there
human: well no one told you that you were going to sit there in the middle of the street
bot: i told you i was like
---------------
Human: Hi, How are you doing?
Bot: good. You?
Human: !!!
Bot: i'm good.
human: great to see you.
bot: i'm going to sleep.
human: next day i was going to go to work, and a friend call me, but i'm too tired.
bot: i'm
---------------
Human: Hi, How are you doing?
Bot: good. You?
Human: !!!! you want to **** me.
bot: how do you make me want to **** you.
human: I can't make you want to **** me.
bot: what are you?
human: just a regular human.
bot: i thought it was
---------------
```
some iphone obsession, really found the iphone popping up in all sorts of other prompts, though I would put it here:
```
Human: what Iphone model you got
Bot: iphone 5s.
human: well you should have asked for it
---------------
Human: what Iphone model you got
Bot: iphone 7/8.5/9.5 (2015) 6
---------------
Human: what Iphone model you got
Bot: iphone 5.1. can't find the option, should check for
---------------
Human: what Iphone model you got
Bot: iphone 4 sim card
bot: i bought a sim card 😊
---------------
Human: what Iphone model you got
Bot: iphone 5s
human: it's a good phone man
bot
---------------
```
