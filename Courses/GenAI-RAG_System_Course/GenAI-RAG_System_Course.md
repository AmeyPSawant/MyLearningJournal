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

Retrieval models lacked making sense of the retrieved information.  
These generative models solve the problem by ustilizing completeness, coherence and adaptability.
Generative models such as GPT, T5, BART, etc utilizes attention mechanisms to focus on the important words ignoring other irrelevant terms and predicting one word at a time.
Generative Models breakdown into three main actions i.e. Using Attention, Predicting Next Word, Decoding the Response.

### The Challenge with Generative Models

- Issue with Retrieval - Retrieval Models can retrieve information but lack coherence.
- Analogy - Needs effort ot interpret as they are not pieced together.
- Problem - Cannot retrieve a complete understandable answer without needing to re organize information.

### Breaking Down Generative Models

- Using Attention - It focuses on the most important parts from the reteived information.
- Predicting Next Word - Generates sentences by predicitng oe word at a time, making responses coherent.
- Decoding the Response - Continues word prediction until a full meaningful answer is created.

## Retrieval Augmenting Generation Architecture

### Components of RAG Architecture

- Retrieval Model - It searches the information database for relevant information
- Generative Model - It structures the retreived facts into a cohesive readable response
- Combined Functionality - Together these models ensure that response is accurate and articulated well.

### RAG Pipeline in Action

1. User Input
2. Transform Question into Vector
3. Retrieve Relevant Information
4. Feed Information to Generative Model
5. Generate the Answer
6. Output to User

## First Basic Project - Interactive Q&A System with RAG
### Step 1 - Document Chunking
### Step 2 - Generating Embeddings
### Step 3 - Retrieve Relevant Chunks
### Step 4 - Generate answer using GPT-3.5 Turbo

