# GenAI - RAG System Course

Course Link - https://youtu.be/IRrhpAXib-Y

## NLP

**Text Preprocessing**  
Text processing consits of multiple ways such as lowercasing, removing stopwords, stemming and lemmatization.

**Tokenization**  
Breaking down the sentence to tokens (words) so that the computer can analyze them further.  
Basically it turns text to data for analysis.  
Two types - Word Tokenization and Sentence Tokenization.

**Embedddings**  
Turns words into vectors (numerical data for analysis).  
Similar ot what a encoder does (One Hot Encoding).

## Attention Mechanism

**Why?**  
 Whwn models process the vectors they struggle t odecide what is most important context of the sentence.

**What?**  
 It's a process that helps computers decide what is the important context in the sentence.

**How?**  
 It assigns importance to words in the sentence.  
 It then calculates importance scores.

## Transformers

**Why?**  
 Normal text processing the computers forgot the relation between the words as they kept on processing new words. So instead of processing

**What?**
It helps in understanding and relating an entire sentence rather than words even if the words are far apart.

**How?**
They start by first converting each word into embeddings (set of numbers) and also add a position number to each word.  
 The transformers then use attention to determine which words relate most closely to each other.

## Text Similarity

- Cosine Similarity - It measures the angle between two text vectors and tells how similar the two vectors are.
- Jaccard Similarity - It measures teh similarity between two sets of words by checking how many words are in common.
- Euclidean Distance - It calculates the straight line distance between two vectors, distance ans similarity are inversely proportional.

## Informational Retrieval

**What?**
It is about finding specific information from a large collection.

**How?**
Three steps

- Document Represenatation - Converts vectors to embeddings, basically converts words to numbers (TF-IDF, Embeddingsm, etc.).
- Scoring & Ranking - Use text similaroty scores and rank them, based on the document and query.
- Indexing - It's a table of contents for all the documents to find relevant documents for queries.

## Introduction to Retrieval Models in RAG

Retrieval models help quickly identify the relevant information.  
RAG is a two part process - Retrieval Model and Generative Model

### Types of Retrieval Model

- Traditional - It searches for exact keywords that match the query.
- Dense - It identifies meaning, retrieving related information even with different wordings.

## Traditional Retrieval Models

### TF-IDF

Term frequency is the number of times the word appears in a document.  
Inverse Document Frequency is how rare is the word across all documents.

### BM25

Best Match 25 is built upon TF-IDF with adjustments in frequency saturation and document length normalization.  
There are two key parameters involved -

- k1 - controls the impact of frequency
- b - adjsuts for document length to avoid bias

## Dense Retrieval Models

### Dense Passage Retrieval

It finds information based on meaning rather than eaxact word matches.
It utilizes dual encoder, one for query and one for passages.  
DPR learns relevance with the help of positive and negative reinforcement.

- Positive reinforcement strengthens the connection b/w relevant embeddings.
- Negative reinforcement reduces connections b/w unrelated embeddings.

## Generative Models
