import nltk
nltk.download()

paragraph="""Today, I stand before you to discuss a revolutionary field that has transformed 
the way we interact with computers and understand human language: Natural Language Processing, or NLP.
In an era where communication is the backbone of our society, NLP holds immense potential to
bridge the gap between humans and machines, enabling seamless and meaningful interactions.
NLP is a branch of artificial intelligence that focuses on the interaction between computers 
and human language. It encompasses a wide range of technologies, algorithms, and models designed 
to understand, analyze, and generate human language in a manner that is both accurate and meaningful.
By leveraging the power of NLP, we can empower machines to comprehend, interpret, and respond to our 
language,creating a world where human-computer interaction is more intuitive and efficient.
The significance of NLP extends far beyond our everyday lives. In the realm of information retrieval,
NLP allows us to process vast amounts of textual data, enabling efficient search engines that deliver
relevant results. It enhances the capabilities of virtual assistants, empowering them to understand 
voice commands and provide intelligent responses. NLP also plays a crucial role in sentiment analysis, 
enabling businesses to gauge public opinion and customer satisfaction by analyzing social media posts 
and online reviews.One of the most exciting aspects of NLP is its ability to overcome language barriers. 
By utilizing machine translation algorithms, NLP enables us to communicate with individuals from different 
linguistic backgrounds effortlessly. It has the power to dissolve the boundaries imposed by language, 
fostering global collaboration and understanding."""

sentences=nltk.sent_tokenize(paragraph)
word=nltk.word_tokenize(paragraph)
