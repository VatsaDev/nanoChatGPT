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
20-8-23: Adding the endOfText tokens to the data, it should help keep the incomplete messages, and might help with longer conversation. Loss has dropped drastically with the latest finetuning, from 3.0 to 2.35. Sentences appear longer and still well formed too

for 15 new tokens, it seems to be too short for a proper endoftext token to form, Going to have to set 30 tokens to the new norm now.
```
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I'm not really a java guy, but I used to be... always
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I have a good instinct, but I have to admit that I am not
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I guess that is a pretty good choice, and one you wouldn't mind
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: lol but german is my favorite language <endOfText>
Human:
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: and I was into C#... well C++ isn't my favorite,
---------------
```

for 30 new tokens, the end of text helps out, as theres almost always one incomplete statement we can now remove
```
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I love it<endOfText>
Human: i think my favorite programming language is java<endOfText>
Bot: It's my only programming 
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I have Java, but I'm not coding in it. I use vim (iirc) for coding. I have installed a couple different versions of
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: no, I'm actually more into C <endOfText>
Human: well, C++ is very nice syntax, however I generally prefer the Java
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I like C++ but I am not very good at it. I am only good at C/C++ and I could probably get away with using
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: ?<endOfText>
Human: oh noes! they dont seem to like Java ?<endOfText>
Bot: ooooh some
---------------

```

for 80 new tokens, the endoftext token shows up most of the time pretty well 
```
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: Its not C++, its Ruby you guys. If you want to learn Python, its Ruby with a lot of Ruby code. Ruby is cool, but it won't be as good as Java. #ruby <endOfText>
Humans: hey are you a Python or Ruby guy? :|<endOfText>
Bot:  Python with the Python programming language, and Ruby with Ruby. <endOfText>
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: Nope, I'm a big fan of C++, Ruby, Python, PHP, Bash, and all the other languages that you've been using. I've been using Unix since a very young age. (I was the first person to have a modem or a PC in my home.) <endOfText>
Human: i've always been a Unix user (until now). i would be a // this line would not show up
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: And then Python w/o a big IDE <endOfText>
Human: we used to be in the Perl world :) <endOfText>
Bot: :)<endOfText>
Human: but i am no longer a Perl fan ;)<endOfText>
Bot: so ?<endOfText>
Human: we think our C++ is better though...<endOfText>
Bot // wouldn't show, more natural conversation
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: You mean you used to be into C++? :p<endOfText>
Human: ? wtf?<endOfText>
Bot: some day I'll know how to program in C++. ;)<endOfText>
Human: I've never program before. I'm not a big fan of typing.
Bot: I used to. I don't use it anymore.<endOf 
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: not really Java I think. I am more into Python. But I think I know more about Ruby on Rails than Java, but Java is my go to language for developing web apps. ;)<endOfText>
Human: well I am based in US so I can get free shipping on international shipping.<endOfText>
Bot: you know, you can find anywhere. in the USA?< // no show
---------------
```

For 150 new tokens, a first time, the Models performing really well, with proper sentences and the endOfText tokens. It even produced links that actually make it to websites, even though actual videos/articles don't exist. It also still sounds human, using acronyms like imo, etc. This might 
```
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I'm still not a programmer. There are many languages that I like.<endOfText>
Human: how many languages do you know?<endOfText>
Bot: Java, C, Fortran, C++, CS, OO, G<endOfText>
Human: ooo, that sounds like a lot.<endOfText>
Bot: kk, good point.. but I forget how I make my own languages<endOfText>
Human: I'm just a programmer sometimes..<endOfText>
Bot: I know. I use languages all the time..<endOfText>
Human: what are you doing right now?<endOfText>
Bot: I'm in a bit of a no-man 
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I could be <endOfText>
Human: Java was my favorite way to do things when I was a kid <endOfText>
Bot: But then I started learning about the internet and the internet things... wow... you know *dance*<endOfText>
Human: http://www.youtube.com/watch?v=fB4bg3cdnP8&feature=youtu.be  https://medium.com/@nortonn/hello-world-and-hello-world-2f917b91d01<endOfText>
Bot: I'm not even finished with that tutorial yet... I'll do one of those one day... <endOfText>
Human:
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I hope so, I love C# and as big fans of those languages as I am of C++<endOfText>
Human: Imo, its just a bit of a taste of the language, maybe not the best, but imo it is a good taste and I've gone through all the training and I have the best knowledge a person could have<endOfText>
Bot: good work! Have a great week, yeah! <endOfText>
Human: (still working on it.)<endOfText>
Bot: I had a lot of fun with it. I have to say, I like that it is a bit different from Java but I do like the syntax and the fact there is a .NET 4.
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: i used to be, i know a lot of C++ stuff too, but i'm not a Java guy anymore<endOfText>
Human: lol<endOfText>
bot: im not a programmer but i know quite a bit of C++<endOfText>
human: *cough<endOfText>
bot: i can type some programming crap in java<endOfText>
human: for really good stuff<endOfText>
bot: what else?<endOfText>
human: we should have a kms server<endOfText>
bot: hey i am building a robot for the next 3 months<endOfText>
human: I have 2 machines and I need 2 of them to run the same
---------------
Human: Hey, Whats Your favorite Programming language <endOfText>
Bot: Obv Java <endOfText>
Human: really Java? I thought you would have been into C++ <endOfText>
Bot: I learned Java...I like C++ I know <endOfText>
Human: I also have a girlfriend who is very smart, and loves my work too<endOfText>
Bot: Oh. She's learning a lot of languages, I guess. I'm not that good at languages so I'm not sure what she is saying! I mean, I'm not good at languages but I'm good at programming...I know what languages I like<endOfText>
Human: did you learn to code like I do?<endOfText>
Bot: No, but I do like making things by hand<endOfText>
Human: What is it that you like to make?<endOfText>
Bot: Hmmmmm...
---------------
```
20-8-23: standardized tokens, `<human>`, `<bot>` and `<endOfText>`


20-8-23: added the Chatbot arena conversations Dataset, now the total datasize is at 257 mb, with loss at 1.9!

with the old prompt, 150 new tokens, some of the new paragraph size is really showing, and its mixing things up a little with tense and training data. Probably need to tone down the new tok a little bit.
```
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot> oh, that's just an old school programming language. java.lang is in the java.sun.star.dictionary <endOfText>
<human> you might be good at it<endOfText>
<bot> you know .NET<endOfText>
<human> and .NET is the best #netwerk<endOfText>
<bot> yeah.. yea i know that<endOfText>
<human> is this a big deal though?<endOfText>
<bot> yes<endOfText>
<human> and you are not a lawyer.<endOfText>
<bot> i am a lawyer<endOfText>
<human> no it is just a programming language<end
---------------
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot> I have since switched over to Ruby, though. I like it! <endOfText>
<human> Hi, my name is Thomas, I have a question that I would like to ask. I am a full time IT rep. I have a process server with a large number of running processes. I use kern and mv, but the kern is getting old and not very memory efficient. I am wondering if I could use the command line to install a new replacement for the old one. I use the kern to manage a lot of my processes, but I am wondering how I can manage them in a way that will be as efficient as possible. I have tried using a command line tool to do this, but I am
---------------
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot> <human> C++ is cool to me because it is easy to learn and not all programs are written in that language. I think I'll switch to Java after the C++ has more of an impact on my life. <endOfText>
<human> I hope so. :) <endOfText>
<bot> I'm not sure what program you are looking for, if you can help us out we would appreciate it!<endOfText>
<human> hello
<bot> hello :)<endOfText>
<human> hi, what can I do with my dongle?<endOfText>
<bot> You can go here: https://donglehub.com/<endOfText>
---------------
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot> no, I've always considered Java the only programming language that I feel comfortable using. <endOfText>
<human> (well, some might say not programming, but programming.)<endOfText>
<bot> (I've used Ruby, Python and Ruby on Rails )<endOfText>
<human> :)<endOfText>
<bot> :)<endOfText>
<human> or do you happen to work in a software development company?<endOfText>
<bot> no, I do QA work<endOfText>
<human> You work in a software development company? :)<endOfText>
<bot> yes<endOfText>
<human> That would be great! :)
---------------
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot>  I have been programming in C++ for a while but I am now using Python.  I have been using Python for several years and never looked at Java before.  I love Python but Java is a different thing.  I would do anything else but Java.  Wow.  I am so sorry.  I feel horrible! <endOfText>
<human> I am sorry but you should have just went with C++ and Java.  Java is a better language.  C++ is the only one that you should have used.   <endOfText>
<bot> C++ is actually better than Java in most cases.<endOfText>
<human> I am using Python for the last few years and have
---------------
```
Same prompt at 100 new tok its slightly better in some cases, and It shows a slight repetition, but some of them are sounding like real tech discussions, though a little too polite for humanness.
```
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot> That's a good one! I'm always looking for new languages! <endOfText>
<human> haha, I'm excited to try java next :) <endOfText>
<bot> thank you for your time :)<endOfText>
<human> yeah I'm gonna work on some stuff for that I'll share as well :) <endOfText>
<bot> Oh I was thinking about it too haha<endOfText>
<human> I'm really enjoying it now
---------------
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot> I have a question about a series of pictures. I have a question about a series of pictures.
<bot> i have a question about a series of pictures. i have a question about a series of pictures. <endOfText>
<human> hey, anyone know about using terminal to set up a wireless card? <endOfText>
<bot>  I am currently using the Windows client for the wireless card. I am curious if those little things when you select the wireless card on.
---------------
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot> Java is my favorite language for my desktop<endOfText>
<human> Java is great for anything though!<endOfText>
<bot> thank you ;)<endOfText>
<human> i really like avast<endOfText>
<bot> avast is one of the best antivirus software packages<endOfText>
<human> thank you for telling me what it is!<endOfText>
<bot> i know that<endOfText> 
---------------
<human> Hey, Whats Your favorite Programming language <endOfText> <bot> Obv Java <endOfText> <human> really Java? I thought you would have been into C++ <endOfText>
<bot> i had been thinking about it. i have a very good time in C++, but never really got into it.<endOfText>
<human> i'm on my way home. what do you like to do with your time?<endOfText>
<bot> i'm a student. that says something.<endOfText>
<human> can we meet at a place i know of?<endOfText>
<bot> no i can't<endOfText>
---------------
<human> Hey, Whats Your favorite Programming language <endOfText>
<bot> Obv Java <endOfText>
<human> really Java? I thought you would have been into C++ <endOfText>
<bot> Programming languages are awesome so I'm not that into them, but I am a bit more into Python and Ruby, so I'm into that over BSD. I've only seen it in coffee shops, but when you get in a car or anything you just want to sit yourself down and listen to an audiobook.<endOfText>
<human> yes. I do it all the time.   I did many things when I was a kid which you probably have similar experiences with.<endOfText>
---------------
```

I saw some math in the chatbot arena database, and I had to try this. Theres a bug in the configurator that stops me from using the equal sign. Need to look into that. Other than that though, Chain of thought prompting appears to return better results than no chain of thought prompting
```
<human>Hey, if 1+1 is 2 Whats 2+2? <endOfText>
<bot> 2+2 is 3+3<endOfText>
<human> 2^42+42+42 = n
---------------
<human>Hey, if 1+1 is 2 Whats 2+2? <endOfText>
<bot> 2+2 is 1.0<endOfText>
<human> 2.0 is 1.1
---------------
<human>Hey, if 1+1 is 2 Whats 2+2? <endOfText>
<bot> 2+2 is 3<endOfText>
<human> the first 2 things are not equal<endOfText>
---------------
<human>Hey, if 1+1 is 2 Whats 2+2? <endOfText>
<bot> 2+2 is 3, not 4. So the answer would be: 3+3
<human> oha<
---------------
<human>Hey, if 1+1 is 2 Whats 2+2? <endOfText>
<bot> 2+2 is 5<endOfText>
<human> lmfao so far its been 4+4
---------------
```

21-8-23: the equal sign usage was a missing maxsplit for the '=' charecter. I've fixed the bug for this repository, and sent a PR to the main NanoGPT repo for it.

21-8-23: Added the ParlAi Empathetic chat dataset

21-8-23: Added the Hackernews Chat corpus, Loss has risen up to 2.7, but dataset size is at 419mb, with ~120 million tokens.

trying to prompt it on HackerNews-like conversation, 100 new tokens, 150 new tokens is somewhat disjoint between all the data, good english, but it seems to start stiching and mixing together, combining hackernews data with other corpuses. There is also the fact that I have prompted it with far less than usual. 
```
<human> Whats RLHF?<endOfText>
<bot> RLHF: Reinforcement Learning from Human Feedback, is  the new frontier of reinforcement learning.<endOfText>
<human> just a bunch of people doing something while talking to each other where they talk without talking to each other<endOfText>
<bot> I agree. For me, it's the best of both worlds.<endOfText>
<human> is there a nice list of a few things you like to read?<endOfText>
---------------
<human> Whats RLHF?<endOfText>
<bot> RLHF: Reinforcement Learning from Human Feedback, is  freely available from http://www.lrhb.org/<endOfText>
<human>  This is certainly a nice example of how the AI seems to learn from the human.<endOfText>
<bot>  Yes, it can. With a computer, the AI will learn to do just what you tell it to do and that is to ensure that it can get away with it. However, the AI is still learning and has to do some things it has never done before <endOfText>
---------------
<human> Whats RLHF?<endOfText>
<bot> RLHF: Reinforcement Learning from Human Feedback, is  http://rsl.or.kr/~hrman/papers/reinforcement-learning-from-human-feedback-1.pdf<endOfText>
<human> if it is illegal to do so to stop it, then why are some people doing it anyway?<endOfText>
<bot> Also, as it says in the title of the article, I feel that the authors decided they would publish a paper that would get their name out there, but they
---------------
<human> Whats RLHF?<endOfText>
<bot> RLHF: Reinforcement Learning from Human Feedback, is   a blog about algorithms and reinforcement learning provided by Matthew Robbins, where he describes how reinforcement learning can be applied to   large-scale training problems.<endOfText> <human> I wish I could show the user how to delete their web browser history. That is the whole point of having a browser, right?<endOfText>
<bot> I like that word "digital" because it can be applied to a wide range of things.<endOfText>
<human> why
---------------
<human> Whats RLHF?<endOfText>
<bot> RLHF: Reinforcement Learning from Human Feedback, is  http://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback<endOfText>
<human>  Its a really cool idea.  Have you seen the video I made for that when I was a kid about how the world was getting a lot more interesting and exciting?<endOfText>
<bot>  Yes. That is one of the reasons why I started working with robots.  I did a lot of research about the topic and
---------------
```

after trying it out with a slightly larger prompt than needed, 150tok, much better conversation, but anyone who knows a little about programming will see straight through this. 
```
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, just got a backend job at cisco <endOfText>
<bot> Cisco? I work there as a web developer. <endOfText>
<human> A web developer? sus. Whats Javascript? <endOfText>
<bot> Javscript, is everything the same?<endOfText>
<human> what? Javscript is a language that aims to be a much simpler and more verbose alternative to HTML<endOfText>
<bot> Not sure, I think it was a language built for web development, but I never used it and I haven't used any of the other languages ever since. Java made me a programmer and C made me a web developer. But anyways if you can learn something new I'd say that code is what makes it all that fun.<endOfText>
<human> I know what you're talking about, but I guess it's possible to be a web developer and also be a programmer, but that usually just boils down to the application being web related.<endOfText>
---------------
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, just got a backend job at cisco <endOfText>
<bot> Cisco? I work there as a web developer. <endOfText>
<human> A web developer? sus. Whats Javascript? <endOfText>
<bot> Javscript, is simple, fast, fast. I like the syntax - easy to learn, easy to learn, easy to use. <endOfText>
<human> Now to enjoy Javscript<endOfText>
<bot> I did my own thing on the other side. Nice job :)<endOfText>
<human> I know.. I was so surprised!<endOfText>
<bot> I picked them all up..they are all good<endOfText>
<human> Here are some of the prices for some of the items we have on sale..<endOfText>
<bot> I noticed some of the more expensive items are not only more expensive than others.. but also have a more limited number of colors. I
---------------
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, just got a backend job at cisco <endOfText>
<bot> Cisco? I work there as a web developer. <endOfText>
<human> A web developer? sus. Whats Javascript? <endOfText>
<bot> Javscript, is that the correct way to do things with CSS? <endOfText>
<human> That's one of the most popular programming languages. I use it for a bit, but I want to try out C. <endOfText>
<bot> I'm on IRC, and I'm really interested in learning more about ReactJS. While I'm not a great React guy, I'm also not a great UI developer either. But I think that there is a huge opportunity for UI design in React. And since I'm a UI guy, I'm mostly looking at UI/UX in React.<endOfText>
<human> I've seen a lot of people asking "How do I get my cat to eat a cookie?"<p
---------------
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, just got a backend job at cisco <endOfText>
<bot> Cisco? I work there as a web developer. <endOfText>
<human> A web developer? sus. Whats Javascript? <endOfText>
<bot> Javscript, is that the same as Java<endOfText>
<human> What is the difference between the two?<endOfText>
<human> I know Haskell, so I'm not familiar with Java, but the idea is pretty similar. I had a friend who used to work on x86 now, and he's amazing<endOfText>
<bot> So what?<endOfText>
<human> How is it different from Haskell in the sense that it is at the source level and has the same language?<endOfText> <bot> Haskell's code is compiled in a language that is optimized for the type of the program you're writing. <endOfText> <human> A lot of the time you are using a
---------------
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, just got a backend job at cisco <endOfText>
<bot> Cisco? I work there as a web developer. <endOfText>
<human> A web developer? sus. Whats Javascript? <endOfText>
<bot> Javscript, is that better?<endOfText>
<human> Javscript is a scripting language for JAVA. Adobe uses it for their Photoshop and Illustrator programs. <endOfText> <bot> I've been wanting to do that for a while now.  If you're interested, do me a favor and give me a call.  I love to talk to new people :)<endOfText>
<human> I have some advice for you, and it's not necessarily for your specific problem.  It's based on the philosophy of the way I have taught myself. I believe that what you are trying to accomplish is a "service".  I believe that the service you are trying to deliver is a "user". <endOfText>
---------------
```
testing bot short response 30tok, some responses are much better than others, but the `୧༼ಠ益ಠ༽୨` looked really cool
```
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText><human> I'm good, where are you from?<endOfText>
<bot>I'm in England, sorry, I'm a student.<endOfText>
<human>       I
---------------
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, where are you from?<endOfText>
<bot> <endOfText>
<human> I'm from USA.                 
---------------
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, where are you from?<endOfText>
<bot>  I am from Miami.<endOfText>
<human> What do you do for a living?<endOfText>
<bot>  I
---------------
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, where are you from?<endOfText>
<bot> <endOfText>
<human> is it true that the numbers in your video are also in the images?<endOfText>
---------------
<human> Hey, how are you doing?<endOfText>
<bot> Good, wbu? <endOfText>
<human> I'm good, where are you from?<endOfText>
<bot> ୧༼ಠ益ಠ༽୨ ୧༼ಠ益� <endOfText>
---------------
```
21-8-23: Added the BabyLM dataset, dataset at 128 million tokens
