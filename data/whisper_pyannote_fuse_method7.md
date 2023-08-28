__SPEAKER_01__ _(0h 0m 0.25s-0h 0m 22.04s_):

Hey, what′s up everyone, this is Sam. In today′s interview, part of our guest
host series, you′ll hear a conversation led by longtime friend of the show, John
Bohannon, Director of Science at Primer AI and former journalist for
publications like Science Magazine, Wired, and others. I′m sure you′re going to
enjoy this conversation, so let′s jump in. Peace.

__SPEAKER_00__ _(0h 0m 24.50s-0h 0m 24.80s_):



__SPEAKER_00__ _(0h 0m 32.50s-0h 0m 33.44s_):

Good morning, Marti.

__SPEAKER_02__ _(0h 0m 33.78s-0h 0m 34.62s_):

Good morning, John.

__SPEAKER_00__ _(0h 0m 35.15s-0h 0m 52.28s_):

So we are just a few miles away from each other across a body of water. I′m in
San Francisco. You′re across the bay in Berkeley at your office at University of
California, Berkeley, where you are the head of the School of Information and a
computer scientist who′s been in the game for many decades.

__SPEAKER_02__ _(0h 0m 52.28s-0h 0m 52.89s_):

That′s right.

__SPEAKER_00__ _(0h 0m 52.89s-0h 1m 12.14s_):

So I′m excited to finally do this interview because it′s been almost a year in
the making. We had a great interview here on the show with Orin Etzioni, former
head of AI2 in Seattle. After that interview, I asked Orin who would be a really
good guest who would have something worth sharing with the audience, and you
were the first person he said.

__SPEAKER_02__ _(0h 1m 12.21s-0h 1m 24.63s_):

Well, I listened to that interview, and it was an excellent interview. Orin is
so articulate, and you′re a great interviewer. I′m really honored to be here,
and I′m really honored that Orin thought it was worthwhile to recommend me.

__SPEAKER_00__ _(0h 1m 24.74s-0h 1m 27.50s_):

You don′t do that many interviews, from what I gather.

__SPEAKER_02__ _(0h 1m 27.65s-0h 1m 49.04s_):

No, I don′t. I′m a little bit camera shy, even though I do have to be on camera
a lot. Also, I like to be pretty careful about what I say, kind of more from the
scientist′s perspective. I think Orin is really great at linking science to
business and where technology is going. But yeah, I guess I′m just a little bit
shy that way.

__SPEAKER_00__ _(0h 1m 49.21s-0h 2m 30.25s_):

And that brings me to kind of the big story here. For those listening at home,
Marty and I had a chat recently in advance of this interview just to talk about
what we might talk about. And something really striking was that there′s this
moment, let′s call it the chat GPT moment, it′s really the large language model
moment, where artificial intelligence seems to be at some kind of inflection
point. And you told me about your long career and how you have kind of seen
these moments before, and you′re more cautious about speaking publicly to add to
the hype cycle because it′s often disappointing and often regrettable. It′s easy
to say things that you later think were overhyped. Why is this different?

__SPEAKER_02__ _(0h 2m 30.32s-0h 3m 30.38s_):

Yeah, so I have seen a lot over the years. I′ve been, I′d say, primarily in
natural language processing, that part of AI. And it′s just been a slog in terms
of making progress and having machines be able to process language the way
people do. I entered it really because I was interested in the brain and
interested in language and I thought it would be kind of neat if we could have a
computer do something with language, maybe make cartoons speak, something like
that. Animation interested me as well. We′re so far from accomplishing anything
that would be realistic that was more of a scientific endeavor. I think I′m more
of a scientist at heart than, you know, I′m not an entrepreneur, for example. So
I′ve seen claims, for example, I remember, I guess in the early 90s, there was
this claim that it was going to transform everything. And it was just so
obviously ludicrous. But you also see, you know, I remember when WebFountain
came out with IBM and that was going to transform everything. And, you know,
it′s very much...

__SPEAKER_00__ _(0h 3m 30.20s-0h 3m 31.51s_):

Or how about IBM Watson?

__SPEAKER_02__ _(0h 3m 31.51s-0h 4m 16.51s_):

Well, you know, Watson was a special case in that it was amazing what they did
with Jeopardy and we can talk about that a bit more. But then there was the
claim that it was going to transform healthcare. And again, there was no path
from that to directly to healthcare being transformed in the immediate future.
So I learned that if you read the New York Times regularly, as I do, technology
is in the business section as opposed to the science section. And that′s kind of
how technology is talked about in, at least in the US. And of course, there is
scientific reporting on it. And your podcast, I think, is wonderful in that it
goes into a lot of technical details, which is really exciting. But there′s
always the business angle when it comes to technology, even when I started out
in the late 80s and, you know, at most there were PCs.

__SPEAKER_00__ _(0h 3m 42.28s-0h 3m 42.48s_):



__SPEAKER_00__ _(0h 3m 56.56s-0h 3m 56.70s_):



__SPEAKER_00__ _(0h 4m 16.78s-0h 4m 38.87s_):

Well, in the late 80s and into the 90s, you became one of the main researchers
in search. And search really defined the era that I think is probably coming to
a close, the Google era, the era of search, search driving everything. And so
you did really see the business side of your research explode and change the
world. Are we in a moment like that now?

__SPEAKER_02__ _(0h 4m 39.12s-0h 5m 52.60s_):

Well, I wouldn′t mind talking about search for a few minutes since it is close
to my heart. I mean, I was interested in search because I wanted to be able to
find things. I didn′t like the library catalog when I was a little kid. And in
fact, when I was an intern, I tried to be an intern in my public library in high
school and I was rejected because I wasn′t fast enough with filing
alphabetically in the card catalog. But I never thought that makes sense. So
actually, I always wanted to do a dynamic, smart version of the card catalog,
which is what I did in search user interfaces. There′s only one spot in the
bookshelf for the book representation. What I focused on was search user
interfaces. I wouldn′t say I was the leading person in search, but I was a
leader in search user interfaces, which was kind of a hybrid topic at the time
because most of the search field was more on algorithms and not so much on the
user interface. So I brought those two together. And that was super exciting
because the technology or the kind of framework that I worked with, did become
the standard for it′s still a standard faceted interaction, what you see on a
website when you′re shopping or library catalogs where you can slice and dice
and filter in different ways to find the items that you want. Getting that
interface to work well was a big challenge and that was sort of the
breakthrough.

__SPEAKER_00__ _(0h 5m 52.70s-0h 5m 56.32s_):

What was the big problem with search interfaces before you got into the game?

__SPEAKER_02__ _(0h 5m 56.73s-0h 6m 57.38s_):

Well, when I got into the game, most software did not have search full stop. I
mean, if you had an application, you couldn′t search for material within it. It
was just rare. It just didn′t happen much. When I got into the game, library
catalogs were searched by saying, you know, PN Bonneman comma J to find the
personal name of the author. I mean, it was command lined. And then there were
Westlaw and these very expensive tools that you could subscribe to, say if you
were a lawyer, it was all keyword based. But the interface, there was no thought
to the interface. It was just a listing of the output that you got, usually in
chronological order. And so there was just no there there. The web changed
things, but even with the web, the initial search was, you know, the blue links,
which has actually been really hard to improve on. And I would say until now,
which we could get to the new moment, you know, Google′s inched towards showing
answers to questions. But I remember talking with someone there saying that they
were conservative initially because they didn′t want to show incorrect
information. And I thought that was the right way to go.

__SPEAKER_00__ _(0h 6m 55.64s-0h 6m 56.00s_):



__SPEAKER_00__ _(0h 6m 57.38s-0h 7m 9.00s_):

Isn′t that one of the big shifts? It′s like once upon a time, the purpose of
search was to find a document or find a resource. But nowadays you want the
answer to a question. It′s almost a shift in intention.

__SPEAKER_02__ _(0h 7m 9.19s-0h 7m 15.79s_):

Actually, I speak to that. I think people always wanted to ask questions, but it
wasn′t possible to get an answer. So

__SPEAKER_00__ _(0h 7m 15.79s-0h 7m 17.81s_):

we were just adapting to a bad system.

__SPEAKER_02__ _(0h 7m 18.05s-0h 8m 9.91s_):

Well, I always like to use the example of this old website called Ask Jeeves,
which was an attempt to allow people to ask questions and get answers. And it
didn′t work because the technology didn′t work, but people kept using it and
always said they liked it because they liked the idea of being able to ask a
question and get an answer. And I have some old screenshots of it. It just
didn′t work. It′s like someone saying, oh, people like the mouse, but now we
have touchscreens and their tastes have changed. I′m like, no, no. It′s that we
didn′t know how to do touchscreens. We didn′t know how to do gestures.
Technologically, in the early days, it was a bridge to that. So often the
interface we see now is the interface people always wanted, but we didn′t have
the technology to support it. And I′d say that′s true for question answering.
Now, there′s an exception for scholars and people doing research who want to see
the documents and primary resources, but that′s always been a minority.

__SPEAKER_00__ _(0h 8m 9.94s-0h 8m 22.67s_):

Yeah. So that brings us to the current moment where the machine behind your
screen that′s going to try and answer your questions is suddenly, and I really
mean suddenly, able to answer it almost like a human it feels like at times.

__SPEAKER_02__ _(0h 8m 23.08s-0h 9m 34.24s_):

I agree. I think it′s a sea change. So I gave a keynote talk in October to the
Information Visualization Society, the IEEE Society. And in that talk, part of
what I did was talked about, you know, this is coming. We are going to see,
instead of people developing visualizations manually, it′s probably going to be
done with text interface. And that′s a pretty radical thing to say. And it was a
month later that ChatGPT came out. And again, I told the audience at that time
that I′ve been in the NLP field for more than years, maybe years, and I′ve never
said this is a major change. And I say it now, I was saying it right before
ChatGPT, and it is transformational in terms of what we can do with processing
language and producing language. It′s not transformational in everything, as
some of the hype says. Just like we had a mouse, and then we had a touchscreen.
We had keyword query or statistical ranking, or we had these very complex
pipelines for making natural language processing systems. And now it′s kind of
one relatively simple architecture that does everything as opposed to specific
algorithms. And it′s kind of head spinning, really.

__SPEAKER_00__ _(0h 9m 34.48s-0h 9m 41.90s_):

Well, simple schematically, but very complicated in terms of what structure
might be hidden in all those billions of neurons.

__SPEAKER_02__ _(0h 9m 42.53s-0h 9m 56.08s_):

Yeah, it′s simple in terms of what the people have to do and complex in terms of
what the program is doing. I actually have an example that I was just trying
last night, because in the same talk, I gave an example of comparatives being
very difficult to process automatically.

__SPEAKER_00__ _(0h 9m 55.73s-0h 9m 56.73s_):

What′s a comparative?

__SPEAKER_02__ _(0h 9m 56.73s-0h 10m 51.31s_):

So if you have, say, a review of a camera and someone in their regular casual
language is saying, oh, the DLSR has a wider angle, but the pixels are not as
crisply retained. What are they saying is better than what? There′s a lot
implied there, and there′s an implicit comparison between kind of the overall
merits of some camera and then these specific components, the pixels and so on.
And I used that as an example of something that would be very hard to write an
algorithm to process automatically. And one of the reviewers of the paper that I
wrote said, yeah, that was true, but I just put this in ChatGPT and it worked
really well. So last night, I put all these super complex descriptions of
reviews of cameras in ChatGPT, and it did an amazing job of saying what was
being compared to what. But I still say that it would be very hard to write an
algorithm to process the language to do that.

__SPEAKER_00__ _(0h 10m 51.20s-0h 10m 51.94s_):



__SPEAKER_02__ _(0h 10m 51.94s-0h 10m 56.56s_):

It′s a general purpose tool that does that as a side effect of what else it
does.

__SPEAKER_00__ _(0h 10m 56.80s-0h 10m 59.43s_):

Yeah, it′s sort of an all-purpose reasoning machine.

__SPEAKER_02__ _(0h 10m 59.56s-0h 11m 3.35s_):

It′s something. I don′t know what it is.

__SPEAKER_00__ _(0h 11m 3.35s-0h 12m 52.76s_):

So I watched your keynote and found it really, really remarkable. And something
that was gestating in my mind as I watched you walk through all the latest
research that you could dig up on the human-computer interface and also language
and the visual component of people trying to understand complex topics was that
we′re probably soon heading into a world where you essentially go to a
whiteboard with a model like ChatGPT. So at work, when I need to understand
something really complicated or communicate something really complicated or
collaborate with someone on a really complicated problem, we go to the
whiteboard. It′s sort of the best environment to do this. What that means is you
have all the affordances of language, just speaking one-on-one, and you also
have this whiteboard next to you that you can diagram things, correct things,
point things out visually. And so it′s sort of maximum bandwidth, and it feels
like the most comfortable way to navigate really complicated things. I think
that we′ve clearly gone way down the road of the chat side of this, the language
side of this. You can interact with ChatGPT and talk about really complicated
things, maybe even solve problems together. But there isn′t yet that whiteboard,
but I think it′s safe to say that we′re headed towards AI whiteboards. And you
have been grappling with the nuts and bolts of how you communicate both visually
and with language, and how the two play off each other, sometimes
synergistically. I′d love to pick your brain just on what it′s going to mean
heading into a world of AI whiteboards. And of course, it goes way beyond
whiteboards. It can show you arbitrary images, videos it generates, things it
finds from the internet, and actually points things out and illustrates it.

__SPEAKER_02__ _(0h 12m 52.96s-0h 13m 39.87s_):

Yeah, I think that there′s a lot of potential for these tools, these large
language model-based tools, to be collaborators in thinking. I think that′s what
you mean by the whiteboard. Yeah. But after I had done my keynote, I did
actually ask ChatGPT to make an outline of a talk on the subject that I had
selected. And it was not very creative. It said things that made sense, but it
would have been, I guess, somebody who kind of knew the field, but was not
innovating, was not seeing the future. And so, I don′t know that it′s capable of
doing that. Yet, I listened to the interview with Sergey, and he, here at
Berkeley, Sergey Levin on reinforcement learning, and he kind of pointed out
that it′s not using technology to kind of do future sequencing. But they′re
working on it, I guess, or they might work on it.

__SPEAKER_00__ _(0h 13m 3.58s-0h 13m 4.09s_):



__SPEAKER_00__ _(0h 13m 39.87s-0h 13m 54.62s_):

Yeah. No doubt the human is going to have to do most of the intellectual heavy
lifting in the beginning. I mean, what is it going to mean for information
sharing and explaining when we can use something as powerful as ChatGPT in the
language regime, also in the visual regime?

__SPEAKER_02__ _(0h 13m 54.91s-0h 15m 4.51s_):

Yeah. So, and referring back to that keynote a bit, the topic is the
intersection of language and visualization. Because the information
visualization community focuses reasonably on how to visualize data, how to
visualize information. And there′s been less of a focus of how does language or
text overlay on that or interact with that. And I mentioned this in our earlier
conversation with John, that for many semesters or many years, I was teaching
natural language processing in the fall and information visualization in the
spring, and thinking about what sort of information can be represented in each
modality. And can you convert one to the other directly? And I think the answer
is no. They show or they explain different visuals, explain different things
than text. And if you think about the movie versus the book, that′s like the
best example. There are some books written to be made into movies. You think
about the Harry Potter series, for example, and they′re very true to the
original, I think. But there′s a lot that don′t transfer so well. And a lot of
it is about interiority and mood and things like that, that mood is expressed
differently with words than with images. And they complement each other, of
course, which is why the soundtrack is so important for the film. When you
become a novelist, you don′t have to write pictures in your novels anymore.

__SPEAKER_00__ _(0h 15m 4.56s-0h 15m 21.75s_):

Except you pointed out in your keynote that really lovely classic book by Scott
McCloud on how comic books work. You pointed out that there′s a method to it.
There′s a kind of balance between the visual and the language. And sometimes one
can do most of the work and sometimes the other. Couldn′t a model learn to do
that?

__SPEAKER_02__ _(0h 15m 21.90s-0h 16m 7.09s_):

Oh, well, could a model learn to do that? I mean, I think you could give it
instructions to learn to do that. I think right now what I′m interested in is
how do people understand these things and then how best to express information
so that you promote understanding and you don′t promote misinformation or you
try to combat misinformation. I think it′s really important that we understand
how, and this is the human computer interaction, the HCI side of the AI HCI coin
as I think about them, understanding how people understand things so that we
know what to tell the computers to do. Right now we have people designing
visualizations and they don′t necessarily know how to put the design into
language and neither will probably the computer. Or if the computer does know,
we at least need to know how to assess if it did a good job or not, which I
think we need to do more work on.

__SPEAKER_00__ _(0h 16m 7.16s-0h 16m 50.62s_):

Yeah. But just to go out one step out onto the limb, I know you′re very wary of
speculation, but this one feels like a safe speculation. I think that there are
going to be emergent capabilities with multimodal models that can deal both with
the visual and the language side. We don′t know exactly what they′ll be, but if
we follow the trend with GPT-3 solely on the language side, I wonder what kind
of capabilities even are there to acquire on the visual side. Something that
comes to my mind is simplifying something visually. Sometimes as simple as
underlining something can make something salient that helps explain the whole.
You have a project called ScholarPHY with Andrew Head at Berkeley. Is he a
student of yours?

__SPEAKER_02__ _(0h 16m 50.84s-0h 16m 59.27s_):

He was a student and a postdoc, and now he′s a professor at UPenn. And it was a
collaboration with people at AI2, hence the Oren reference.

__SPEAKER_00__ _(0h 16m 54.29s-0h 16m 55.40s_):



__SPEAKER_00__ _(0h 16m 59.34s-0h 17m 25.44s_):

I saw a breakdown of the project. It′s so neat. One of the really neat insights
is when you read something that′s got a lot of complicated mathematics in it,
your brain is doing a ton of work behind the scenes. If you had a better
interface, for example, click on a variable in a formula and just have it
automatically pop out and say, this is what that represents. So you offload some
of that cognitive work you have to do. I wonder if those kind of skills could be
learned.

__SPEAKER_02__ _(0h 17m 25.62s-0h 17m 29.72s_):

I hope so. And you mean the skills of visually showing the information?

__SPEAKER_00__ _(0h 17m 29.24s-0h 17m 33.83s_):

Yeah. All those tricks that a good visual explainer just knows how to do.

__SPEAKER_02__ _(0h 17m 34.16s-0h 18m 27.16s_):

Well, I am optimistic that these new models will make that automation task that
we had more effective. We worked on algorithms to do it automatically, but PDFs
are really tricky to process if you′re looking at the image level. And it′s very
hard to find definitions within a scientific paper because not everything is
defined in a crisp way. And so really what you want to do is generate your own
text, but you want it to be accurate. It′s based on the text of the paper. So we
are actually looking to see if the latest models can help with the automation of
that task. But going back to a point you made earlier about creativity or new
synthesis with these models, I think someone who was hosted earlier on this
podcast pointed out just even the avocado sofa is a synergy of image. A human
had to ask the query, but then the system was able to blend these images
together into something new. Although it doesn′t blend well if they don′t go
well together.

__SPEAKER_00__ _(0h 18m 27.26s-0h 18m 47.67s_):

In case anyone listening doesn′t know what the avocado chair is, this was the
sort of amazing DALI moment. So the DALI model came with a paper, and in that
paper they had some images as examples of what it could do. And one of them was
make a chair made of an avocado, something like that. And it was sort of
amazingly convincingly good. It really was. Yeah,

__SPEAKER_02__ _(0h 18m 47.26s-0h 18m 56.17s_):

although they are a little cherry picked because if you try to combine two
things that don′t often go well together or don′t appear together, it doesn′t
work, or at least it didn′t work when I was playing.

__SPEAKER_00__ _(0h 18m 56.13s-0h 18m 56.89s_):

It′ll flub it.

__SPEAKER_02__ _(0h 18m 56.89s-0h 20m 23.58s_):

Yeah. But still, it′s a great example of synergy with these tools. And what I
noted in the keynote was that co-pilot these systems that aid in programming
rather than, you know, there′s been a long debate in HCI about when you′re
developing, say, a user interface or doing data analysis, should it be a command
line or should it be a graphical user interface, a GUI? And of course the answer
is neither works perfectly, and people who are practitioners use a blend of
both. But it seems now, as I said about Ask Jeeves, what people really want to
do is just use language to say, do this, do that, and have the program get
written. And then point and use gestures in the interface to tweak it a bit,
this multimodality. And again, there are tools to do that, but they′re just not
perfect. And the more that the algorithms improve, like with ChatGPT, the more
effectively we′ll be able to help people design visualizations where they don′t
have to do a lot of coding. It′s again, because it works, this general purpose
tool that we′re talking about, as a side effect of being, you know, produce the
next word, it′s able to do all these other things, and I think we don′t
understand why, but that includes writing code or, you know, being smart about
adding things into code and so on. It wasn′t designed for that, but it seems
like it will be very effective at making it easier to design visualizations. The
problem is, will it design good visualizations? And, you know, that′s where we
still have the human component.

__SPEAKER_00__ _(0h 20m 23.71s-0h 20m 32.72s_):

Well, I think the safe way to use these things is to generate first drafts and
iterate, but that you have to be the human editor who makes the final call and
do the driving.

__SPEAKER_02__ _(0h 20m 32.76s-0h 20m 45.04s_):

Yeah, I agree. The work that we all do in the viz field can help determine what
makes a good design, help give guidelines. We do research, empirical research,
and then we produce guidelines for practitioners to follow.

__SPEAKER_00__ _(0h 20m 45.23s-0h 21m 23.51s_):

So, bringing this all back to this moment, you′re a natural language processing
practitioner. You′ve spent years trying to teach machines to do useful things
with language. And here we are, in a moment where, I don′t know about you, but I
feel like, wow, a lot of the things we solved, you don′t have to worry about
anymore. Just sort of more and more and more of all that hard, algorithmic,
hand-rolled feature engineering world is getting eaten up by large language
models that can simply speak. And they seem to have cognitive abilities that we
would never have dreamed would be in a machine.

__SPEAKER_02__ _(0h 21m 23.75s-0h 21m 28.81s_):

Well, I′m not going there with you on the cognitive abilities that I′m very
cautious and skeptical about.

__SPEAKER_00__ _(0h 21m 28.51s-0h 21m 30.11s_):

What should we call them? Behaviors?

__SPEAKER_02__ _(0h 21m 30.38s-0h 23m 39.19s_):

I guess I don′t have my favorite word for it yet. Capabilities. It works a lot
better than it used to work. There′s a lot of people looking into, you know, why
does it work? But, you know, each time people start to make some progress on
that, then a new model comes out that′s even harder to understand because the
scale is so much larger and we′re not good at thinking at a very large scale.
So, I think it′s going to take years before we understand what′s going on. I
don′t think it′s cognition. I′m very skeptical about that. It′s really, I mean,
you know, we get into philosophy and the Chinese room, that′s an old John Searle
thought experiment. I mean, it′s unfortunate, I guess, the use of Chinese in
that particular example. But the idea being if you replace each piece of your
brain with a little, like, component, electronic component, and you eventually
replace every piece, is it still a brain? You know, are you still thinking?
There′s philosophy thought experiments. You might want to say, oh, well, this
model that′s basically just a bunch of numbers, a bunch of weights that have
been trained, is thinking because you can say that about the brain. But, you
know, I′m not convinced. I think there′s a lot more going on in the brain than
is going on in these models. They′re very good at mimicking, you know, at
producing language and because language is distinctly human, it feels, you know,
to a lot of people like it′s human. When people are driving in their cars, they
name their car, even old cars that had no electronic components. They would name
their cars. They would anthropomorphize their cars. They feel a part of their
cars. This is what we do with technology. People are going to get used to it and
then it′s going to become old news. And I think it′s great that we don′t have to
write all these tokenizers. The LP pipeline didn′t work. It was a mess. And
there′s always new problems and new questions to investigate from a research
perspective. Researchers will not be out of business. Of course, it does raise
even more societal issues and dangers because of the ability to fake
information, to spread misinformation, and for people to not know what′s real
and what′s true. So we′re living through a very chaotic moment right now. I
think we′re going to look back years from now and we′re going to go, wow, that
was a chaotic time in technology. That was a chaotic time politically. And
hopefully we′ll be able to look back and say, thank goodness we made it through.
I have optimistic we will.

__SPEAKER_00__ _(0h 22m 34.79s-0h 22m 35.49s_):

I agree with you.

__SPEAKER_00__ _(0h 23m 39.41s-0h 23m 54.05s_):

Well, the curve you′re describing is pretty smooth. It implies that there′s
going to be another side to this. But if things keep exponentially changing,
there won′t necessarily be that moment because it′ll always feel like it does
right now.

__SPEAKER_02__ _(0h 23m 54.36s-0h 24m 14.04s_):

Well, the technology that this breakthrough with these models and really with
training on huge amounts of compute, huge amounts of data, I think it can only
go so far. We don′t know the limits of it, but it′s not going to be everything.
If you look at people that are trying to study the brain, you know, there′s
other things going on there, different kinds of structure and so on.

__SPEAKER_00__ _(0h 24m 14.14s-0h 24m 15.52s_):

You think we′re running out of data?

__SPEAKER_02__ _(0h 24m 15.91s-0h 24m 28.15s_):

No, no, I don′t think that′s it. I think that the technique, it′s a very
specific technique. That alone I don′t think is going to be sufficient for being
the same as humans. I don′t say we could ever do it.

__SPEAKER_00__ _(0h 24m 28.23s-0h 24m 36.05s_):

Some people do argue that sequence prediction, which is essentially what is
driving this whole craze, might be all you need. What do you think about that?

__SPEAKER_02__ _(0h 24m 36.44s-0h 25m 39.60s_):

Well, it′s certainly all you need for certain tasks. We′re seeing that now. It′s
really quite amazing. There is sometimes fine-tuning on the other side, but
again, who knows? I personally have been wrong about this particular technology.
I think like a lot of people, I just didn′t know how to think in terms of
billions of parameters and we′re just not good at that. There were some very
ambitious people that just sort of went for it and surprised all of us. I admit
it, I did not see this coming and I was surprised by it. We have certainly in
the research community, it′s been developing gradually. Word2Vec came along.
Going back even farther, again, when I was doing early in the statistical NLP
time, people were looking at SVDs, singular value decomposition, and LSA, latent
semantic analysis, which is similar in a lot of ways. It was putting words in a
matrix, well, words by document matrices and trying to find similarities. Even
before that, I was trying to solve the thesaurus or the synonym problem to help
with search. In search, you look for cat and it′s really feline and you don′t
find anything. Going back to the beginning of our conversation...

__SPEAKER_00__ _(0h 24m 57.38s-0h 24m 57.93s_):



__SPEAKER_00__ _(0h 25m 39.33s-0h 25m 45.37s_):

And you didn′t want users to have to put in every synonym imaginable for a cat
just to find text about cats.

__SPEAKER_02__ _(0h 25m 45.79s-0h 27m 17.30s_):

Well, library catalogs had synonyms in the early days. They weren′t that good,
they weren′t dynamic, they didn′t handle new technology and they were hard to
use. WordNet came along and developed as a linguistic tool and was the first
person to download it, actually, when they had an FTP available. I did work on
that and it was like, oh, we can have a thesaurus. But it never worked. Whenever
you had automatically recommended terms for a term, some of them were right and
some were wrong. That was true of SVD and LSA as well. They worked in some
cases, they didn′t work in other cases. It wasn′t until Word2Vec came along and
then people actually refined it to have different senses that it actually
started to work. I was saying, wow, this actually works and I′ve seen years of
this not working. Of course, that kept being refined and being made more
sophisticated with the transformers came along and now the really large things.
In the research community, it′s been happening gradually. There were a lot of
debates about counting versus probabilities and all this. It′s not out of the
blue, but I do, again, I admit that in this last year between the combination of
the image plus text generation and these language models where the input could
be text, we never thought the input could be text and then the output would be
all these things. We thought we had to program things. I don′t think the people
who developed these models expected that either. I believe it was a surprise to
them. It is different now. I don′t think everything is solved. I don′t think
it′s AGI, but the tools are much more effective than they used to be.

__SPEAKER_00__ _(0h 26m 28.46s-0h 26m 28.63s_):



__SPEAKER_00__ _(0h 27m 10.20s-0h 27m 10.57s_):



__SPEAKER_00__ _(0h 27m 17.47s-0h 27m 45.49s_):

Well, like you said, it′s all about capabilities. It turns out if you teach a
very big neural network how to predict the next word on a huge amount of
internet text, all these really neat emergent capabilities come into your hands.
It couldn′t have been predicted. In fact, no one really thought it would work as
well as it does, I′m sure, but it does. I wonder what happens when you teach a
model to predict the next image in every YouTube video. What capabilities
emerge?

__SPEAKER_02__ _(0h 27m 45.83s-0h 27m 51.85s_):

Yeah, it′s going to be interesting. It should be much better at generating
videos. I guess there′s already work on generating videos.

__SPEAKER_00__ _(0h 27m 51.85s-0h 28m 31.17s_):

I feel like generating videos is kind of like that unicorn story moment.
Remember in the early days of GPT-3 when they were trying to show how great it
was? They said, look, you can start the first sentence of a story about
something that it definitely has never seen. It was something about unicorns. It
could just write a story. It′s where you start with an image and you just say,
hey, finish this. Make this a one-minute video from this scene. That′ll happen.
Just like with GPT-3, the thing that′s going to blow us away are the things we
can′t predict it′ll be able to do. It′s going to have capabilities that just
emerge.

__SPEAKER_02__ _(0h 28m 31.53s-0h 28m 41.03s_):

Well, I have to admit that I was not at all impressed by the unicorn story. In
fact, that′s why I was skeptical. I was like, this is clearly cherry-picked and
it′s from a fairy tale and you put anything else in. It′s

__SPEAKER_00__ _(0h 28m 40.81s-0h 28m 41.72s_):

just not useful.

__SPEAKER_02__ _(0h 28m 42.16s-0h 29m 19.00s_):

Well, when you do NLP, there′s different kinds of tasks. Some tasks are easier
to evaluate than others. Like information extraction, did you identify the right
that a company is an organization or is it a rock band or whatever? If you are
doing search, it′s very hard to know if you have the best ranking in a lot of
cases. If you′re doing summarization, there are many legitimate ways to
summarize a paper. It′s really hard to evaluate summarization. If you′re
generating a story, you can generate almost anything and it′s a story. This is
why I was not at all impressed by the unicorn example, but it turned out that
actually there was more behind it than the cherry-picked example. Although
GPT-3…

__SPEAKER_00__ _(0h 29m 18.85s-0h 29m 25.15s_):

I wasn′t impressed with GPT-3 myself until the instruct GPT version came out and
the thing actually did your bidding.

__SPEAKER_02__ _(0h 29m 25.35s-0h 29m 26.94s_):

Yeah, well, they improved on it.

__SPEAKER_00__ _(0h 29m 26.94s-0h 29m 28.30s_):

Yeah, they really improved on it.

__SPEAKER_02__ _(0h 29m 28.42s-0h 29m 54.87s_):

The problem is initially they were hyping it in ways that weren′t helpful. I
know that now they′re being more careful. I mean, open AI. Or maybe they did
have more behind the scene. They kind of said, oh, well, we know stuff that you
don′t know and we can′t share it. So you want everyone to be able to test
things. That′s what happened with the fake blood testing company It was clear
from the beginning it was fraud. So you have to, if you′re going to make big
claims, you need to be able to show your cards.

__SPEAKER_00__ _(0h 29m 47.91s-0h 29m 48.46s_):

and all that.

__SPEAKER_00__ _(0h 29m 55.11s-0h 30m 15.86s_):

Yep. All right. So zooming out a bit, what do you think is going to be the most
exciting things to pay attention to on the research side of your fields? You
really have more than one field. But I′d love to just hear your thoughts. What′s
in your mind these days given this kind of big sea change as you describe it,
which I agree.

__SPEAKER_02__ _(0h 30m 16.25s-0h 31m 25.76s_):

Well, there′s a lot of people doing a lot of stuff. There′s a lot of people
really interested in AI safety and AI anti-bias. They′re all very important. I
think there′s also a lot of people looking at the AI human interface, which is
something I′ve been interested in for a long time. And that′s super important.
People doing driving cars, self-driving cars have a bit of a head start, mainly
on seeing how hard the problem is. Actually, I had a PhD student at Cecilia
Aragon who looked at projecting LIDAR visualizations for helicopter pilots on
the screen and how could we make that work and have them not crash? Because this
could show them if, say, a squall was ahead and they might potentially crash if
they went into it. And we found that the simplest, most bare-bones interface was
the very best so that they weren′t distracted. So I′ve always had questions
about self-driving cars and that problem of the attention of the driver. And
that′s really not solved. And the studies I have seen on automatically generated
language and interfaces, even some we′ve done in the Scholarify semantic scholar
project, semantic reader project, we don′t have good answers for that. People
just start to rely on the automatically generated output. It′s natural. And so
that′s a huge problem that needs to be solved.

__SPEAKER_00__ _(0h 30m 50.16s-0h 30m 50.64s_):



__SPEAKER_00__ _(0h 31m 25.78s-0h 31m 35.76s_):

What are some of the ways that we could help people if everyone comes to rely on
chat GPT for day-to-day work? What are some of the levers we can pull to help
them?

__SPEAKER_02__ _(0h 31m 36.19s-0h 32m 52.45s_):

I haven′t solved this problem. I mean, it′s certainly good user interface
design, understanding people. So HCI shows us how to study people and how they
work and how they work with technology. So using HCI methods to deeply study
that and in different contexts. It′s different in a medical setting. There′s a
colleague that, Ilifar Salehi here at the iSchool at Berkeley, who is looking at
machine translation in a medical setting and when information is not translated
correctly and how that can adversely impact marginalized communities when the
translation isn′t really the right thing and how to get the context right. So I
think each setting is probably going to need some specialized research. And
furthermore, one of your podcasts is about how do people inject poison, the
training data and so on. And so you're going to have to be very careful about
attacks like that. It′s not a field that I′m in. Perhaps it will be important to
have diversification in the different models so that there′s ways to check them,
make sure that they are safe and appropriate for a particular use. I think the
techniques of HCI and ethnography really work independent of the context. It′s
not AI. People in AI don′t necessarily want to sit down with people, humans, and
see their details and what they do and so on. But that′s the only way to have
really working systems that are good for society.

__SPEAKER_00__ _(0h 32m 52.76s-0h 33m 16.65s_):

Yeah, I′ve noticed that there′s this kind of mindset of people who build AI,
generally people who build AI systems. It′s the engineering mindset. The more
you can take the person out of the equation, the better because I want my
development environment to be nice and clean and straightforward and I want to
build something that I understand. And as soon as you get people involved, oof,
people are complicated. But what you′re saying is you have to include the
person.

__SPEAKER_02__ _(0h 33m 17.11s-0h 33m 46.17s_):

Yeah, and that′s why I′m heartened by the new interest in NLP plus HCI. There′s
been workshops I′ve asked to talk at because I′ve been thinking about it for a
long time. But it′s true that a lot of people who are making the biggest
advances in the NLP AI field are mathematicians or physicists and it′s just not
what they think about. They like to think abstract way and they′re brilliant and
they′re really improving these systems. But we need teams to work on technology.
The one-person band just doesn′t exist in this space.

__SPEAKER_00__ _(0h 33m 46.53s-0h 33m 52.59s_):

So what would you say to students coming into these fields just now? Has the
advice changed at all?

__SPEAKER_02__ _(0h 33m 52.64s-0h 34m 9.10s_):

It′s hard to know what to say right now. It′s moving so fast. What I say to all
students is what are you passionate about? What really interests you? Do that.
Don′t do the trendiest thing for its own sake. It′s definitely a big question
mark right now for research universities and AI labs and other research groups.

__SPEAKER_02__ _(0h 34m 9.87s-0h 35m 22.28s_):

If there′s a big microscope that some people have and you don′t, how do you
compete? There′s open source effort, things that Hugging Face and others are
doing. I think the US government is interested as well in giving everybody a
microscope, meaning these large language models and the ability to run them. I
think that people are very aware of that issue. But then if you want to do
advanced research on this, you get brilliant people like Agent Choi at
University of Washington and AI2 that are showing that you can do a lot with
much less. You don′t need to have all these parameters and so on. That′s where
the university can help. The university people are also going to be looking at
how do you save energy. Well, I mean, so is industry. But how do you save energy
when you use these? It′s very wasteful right now. These are all great areas for
research. Of course, understanding what these models are doing, understanding
the mind better, can they help us understand the mind in some way? I′m sure
psychologists are thinking about that. There′s work already, I′ve seen work in
linguistics on say using GANs and adversarial methods to model linguistics in
other species. There′s always more research questions. If you′re interested in
being in industry and business, then go do that. If you′re interested in
research, then find a problem that just really interests you because that′s how
you can finish your PhD.

__SPEAKER_00__ _(0h 35m 22.60s-0h 35m 32.36s_):

And just to bring it to a close, what′s coming up in your life that listeners
might be interested to know about? Is there a project or an event on the
horizon?

__SPEAKER_02__ _(0h 35m 32.59s-0h 36m 16.92s_):

Well, I think the project that I′m most excited about is working with my PhD
student, Chase Stokes, on understanding this interaction between language and
visualization. We just finished a paper that we submitted on if you place text
on a chart and the goal of the chart is to predict how text impacts that
prediction. Like who′s going to win an election by looking at this chart? And we
actually found surprisingly that the text did not influence the prediction all
that much. In this case, where people relied more on the visual input. But in
another study we did where it was more what are you taking away information-
wise, then the way the text was used did have an influence. So what we really
need to do is understand this interplay more. I′m just very excited about that
topic. I know it′s kind of a niche topic, but it′s what interests me.

__SPEAKER_00__ _(0h 36m 17.01s-0h 36m 31.77s_):

Oh, far from niche. We′re going into a very momentous political year and these
little interactions between a person and a piece of information can have
massive, massive effects. You′re right. We don′t really understand how they
work, do we?

__SPEAKER_02__ _(0h 36m 32.07s-0h 36m 43.93s_):

No. I like to work in topics where there isn′t a lot of work at that time, like
search interfaces and so on. And then when it becomes popular, I tend to move
on. I think I can′t compete or something. So I have to find a new thing that
nobody′s thinking about.

__SPEAKER_00__ _(0h 36m 43.97s-0h 36m 48.56s_):

Uh-oh. I might have just ruined your picnic. Now everyone′s going to get
interested in language and visualization.

__SPEAKER_02__ _(0h 36m 48.56s-0h 36m 53.56s_):

No, no. I want that. In fact, the keynote I gave, I think, helped with that. So
I want people to be working on this.

__SPEAKER_00__ _(0h 36m 53.85s-0h 36m 55.91s_):

Marty, thanks so much for talking with us.

__SPEAKER_02__ _(0h 36m 56.12s-0h 36m 57.62s_):

It was a pleasure. It was really fun.

__SPEAKER_01__ _(0h 37m 0.42s-0h 37m 20.25s_):

All right, everyone. That′s our show for today. To learn more about today′s
guest or the topics mentioned in this interview, visit twimmelai.com. Of course,
if you like what you hear on the podcast, please subscribe, rate, and review the
show on your favorite podcatcher. Thanks so much for listening, and catch you
next time.

__SPEAKER_01__ _(0h 37m 22.99s-0h 37m 25.50s_):



