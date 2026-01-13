# AI ML and Data Analytics

It's composed of three tiers:  
## Tier 1: Pre-built AWS AI services
They provide access to pre-built models that are already trained to perform specific functions.  
These include Amazon Polly for text-to-speech generation, and Amazon Comprehend for text or sentiment analysis.  
The AWS AI Services are further categorized into 3 groups:  
### Language services
AWS AI language services are great for when you need to interpret text or speech and transform it into something meaningful.  
* Amazon Comprehend - uses natural language processing to extract key insights from documents.  
_Use Cases:_ Content classification, customer sentiment analysis, and compliance monitoring.
* Amazon Polly - converts text into lifelike speech. It supports multiple languages, different genders, and a variety of accents.  
_Use Cases:_ Virtual assistants, e-learning applications, and accessibility enhancements for visually impaired users.
* Amazon Transcribe - converts speech into text with the support of multiple languages, and features such as speaker identification, custom vocabulary, and real-time transcription.  
_Use Cases:_ Customer call transcription, automated subtitling, and metadata generation for media content.
* Amazon Translate - is a text translation service.  
_Use Cases:_ Document translation and multi-language application integrations.

### Computer vision and search services
* Amazon Kendra - uses natural language processing to search for answers within large amounts of enterprise content.  
_Use Cases:_ Intelligent search, chatbots, and application search integration.
* Amazon Rekognition - is a video analysis service that can identify objects, people, text, scenes, and activities within images and videos stored in Amazon S3.
_Use Cases:_ Content moderation, identity verification, media analysis, and home automation experiences.
* Amazon Textract - Amazon Textract detects and extracts typed and handwritten text found in documents, forms, and even tables within documents.
_Use Cases:_ Financial, healthcare, and government form text extraction for quick processing.

### Conversational AI and personalization services
* Amazon Lex - can be used to add voice and text conversational interfaces to your applications.  
This service uses both natural language understanding (NLU) and automatic speech recognition (ASR) to create lifelike conversations.  
_Use Cases:_ Virtual assistants, natural language search for FAQs, and automated application bots
* Amazon Personalize - can help build intelligent applications using historical data with personalized recommendations for your customers.  
_Use Cases:_ Personalized streaming, product, and trending recommendations.

## Tier 2: ML services  
Such as SageMakerAI, can be used to build, train, and deploy ML models using fully managed infrastructure, tools, and workflows.  
It also helps in track model training experiments, visualize data, and perform model debugging and monitoring.

## Tier 3: ML frameworks and infrastructure
When a highly specialized ML Solution is required, these frameworks and infrastructure can be used.  
This includes using purpose-built chips that integrate with popular ML frameworks.  
You can even build a solution hosted on an ML-optimized EC2 instance.  


## Generative AI
Generative AI is a type of deep learning powered by extremely large ML models known as foundation models (FMs).  
FMs are pre-trained on vast collections of data.
Large language models (LLMs), are a popular type of FM trained to use human language.  
Foundation models can also be used to create videos, images, music, and more.
* __Amazon SageMaker JumpStart__ — An ML hub with FMs and pre-built ML solutions deployable with a few clicks.
* __Amazon Bedrock__ — A fully managed service for adapting and deploying FMs from Amazon and other leading AI companies.
* __Amazon Q__ — An interactive AI assistant that can be integrated with a company's information repositories.


## Data Analytics
Data analytics is when analysts transform raw historical data to uncover valuable insights and trends. This traditional data analysis can apply to important use cases, such as the following:
* Loan companies explaining lending decisions to customers.
* Medical researchers analyzing clinical trial data through hypothesis testing.
* Insurance companies making their risk assessment models transparent for regulators.

## Using Data Pipelines on AWS
Data can come multiple sources and it needs to stored in a single location.
* **Data Lakes**  
  - Stores raw, unstructured data at scale (e.g., Amazon S3)  
  - Flexible for diverse sources (apps, sensors, streams)  

* **Data Warehouses**  
  - Stores processed, structured data (e.g., Amazon Redshift)  
  - Optimized for analytics/BI  

* **Key Difference**: Lakes keep raw data; warehouses organize it for queries.  

Traditional Data Pipelines consist of
* __Data Ingestion__ - Moving data from source systems to storage  
  * **Real-time**  
    - *Amazon Kinesis Data Streams*: Low-latency processing (e.g., stock market data)  
    - Supports multiple concurrent consumers  
  * **Near-real-time**  
    - *Amazon Kinesis Data Firehose*: Managed streaming ETL (e.g., IoT device data)  

* __Data Cataloging__  
  - *AWS Glue Data Catalog*: Central metadata repository (stores format, location, schema)  

* __Data Processing__  
  * **Basic ETL**  
    - *AWS Glue*: Serverless, visual workflow builder  
  * **Advanced Processing**  
    - *Amazon EMR*: Big data frameworks (Spark, Hadoop)  

* __Querying__  
  - *Amazon Athena*: Serverless SQL for S3/hybrid data  
  - *Amazon Redshift*: Data warehouse for complex analytics  

* __Visualization__  
  - *Amazon QuickSight*: BI dashboards with natural language (Amazon Q)  
  - *Amazon OpenSearch*: Real-time log/operational analytics  
