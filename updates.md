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
20-8-23: I Increased the amount of PersonaChat-Like Content in the Data by a little, but now our model has gone from 700K lines of Data to ~3.6mil lines(187MB data), thanks to the addition of the Ubuntu-Corpus. For a while the model may speak like a linux dev for a while now, the corpus should have bettered the capability, and Val loss values also seem better, down for 3.4 to 3.0. 
Newer Prompts displays

for 15 tokens, mostly great
```
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: lol
human: I'm sorry, I was just thinking for a second.
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: I am not into programming.
Human: :-p
Bot: oh
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: thats java
human: c++
human: its great
human: I like python
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: I was into C++ and Haskell, but C# is the language I
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: yes Java
Human: Java is a Java dialect
Human: so is C++
---------------
```
for 30 tokens, tenses are a little of, but other than that its mostly okay 
```
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: I was
Human: ... C++
Human: No, Java is my go to for programming bots.
Bot: So I'm looking for a programming language
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java?
I thought you would have been into C++
Bot: I am, but I do not use it
Bot: I never really use java
human: I use only pandoc
Human: and Python
Human: I
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: I think im a bit confused with the question, Java is cool though
Human: so if you have a Java Proj, I suggest you get that
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: I'm not very big into java though though
Human: i not quite, but I'm a C++ programmer, and Java is my favorite language
Bot:
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: sorry, I can't think of a reason at the moment
Human: I like to get creative with code, and can live with any language
Human:
---------------
```
for 50 tokens, slightly better off than 30 token on human/bot, but its text is also ok/almost makes sense.
```
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: omg c++?
human: c++ is just something I learned from a college textbook
Human: I was going to say "I learnt C++ from a college textbook" but I'm not quite sure.
Bot: Really, C++, I
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: is Java the only programming language that I've ever used?
Human: Java is the programming language I prefer to use
Human: So yeah, I'm going to use Java.
Human: I am using the official Java IDE.
Bot: Yeah, the
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: C++
Human: i am Java
Human: I have always been a Java guy
Human: I think the others too
Human: I just finished training in Java for a couple years, and learned a lot and am a bit more comfortable with todays languages
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: I am not (don't know) but Java is my go to engine for the most part
Human: I LOVE Java and Love Programming in general, but I don't know how to get a good Java job despite learning to code.
Bot:
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: C++
human: yes I am in :)
bot: then I am in :)
human: was going to ask something about the language but I dunno how to ask
bot: they do not have a forum for it
human: we use a forum already
human:
---------------
```
for 80 tokens, tense really improved at this point, some of these conversations might actually pass for regular forum conversations to non-techies
```
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: C I am not a c++ guy
Human: I think that's a good way to define a programming language
Human: Java is one of the best languages I have ever used
Bot: I think I prefer Scala
Human: Java is one of the best languages I have ever used
bot: Scala?
Human: and I use Gulp
Human: and I'm paying just $10 to use it?
Bot:
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: I am a Java programmer
Human: I think Java is a great language
Human: it is not a 'language' though
Human: I guess you are right
Human: but Java is awesome in my opinion :)
Bot: I look at it with a rather more critical eye
Human: and thats what you are doing is wrong
Bot: I see you are really anti java
Human: I wasnt anti java I
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java?
I thought you would have been into C++
Bot: I'm not sure, maybe C#
Human: I like the Quake series though
Bot: Does anyone know anything about the F-35?
Human: Oh well, I think I know a few things.
Bot: Well, you should check out www.ff.org
Human: ok, I'm out of Google, sorry for the confusion I guess.
Bot: So you have a BBS?
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: Im not so much an expert in programming, but I can understand from a scripting standpoint.
Human: I've never been a huge fan of Java either but I like Ruby and Python.
Bot: I think Java is a great language and I would say a great programming language. Human: I thought Python was a great language too, but I like Lua.
Bot: I mean, I'm a
---------------
Human: Hey, Whats Your favorite Programming language
Bot: Obv Java
Human: really Java? I thought you would have been into C++
Bot: hello Rob: i need a real job, not just an internship.
Human: not at all
Rob: hahah you should've just said which is your favorite language
human: and you would have been right
human: the only language i actually like is python
Human: lol bot, i like python. i like to learn stuff
human: i'm not a good developer
human: i just like to
---------------
```
