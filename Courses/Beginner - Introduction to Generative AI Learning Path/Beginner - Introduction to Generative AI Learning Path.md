# Beginner: Introduction to Generative AI Learning Path
## Introduction to Generative AI
- **Generative AI Definition and Functionality** Generative AI is a subset of artificial intelligence that creates new content—such as text, images, audio, and video—by learning patterns from existing data. It uses models like neural networks and transformers to generate outputs based on input prompts, distinguishing it from discriminative models that classify or predict data.

- **Types of Generative AI Models** Generative AI encompasses various model types, including text-to-text, text-to-image, text-to-video, and text-to-task models. These models can perform tasks like language translation, image generation, video creation, and executing specific actions based on textual input.

- **Applications and Tools** Generative AI has broad applications across industries, from healthcare to customer service. Tools like Google’s Vertex AI Studio and Gemini enable developers to build, fine-tune, and deploy generative AI models, even with minimal coding experience, facilitating tasks like code generation, sentiment analysis, and personalized customer interactions.


## Introduction to Large Language Models
- **Large Language Models (LLMs) Overview** LLMs are a subset of deep learning and generative AI, designed to process and generate human-like text. They are pre-trained on massive datasets and fine-tuned for specific tasks, enabling them to perform a wide range of language-related functions such as translation, summarization, and question answering with minimal domain-specific training.

- **Key Features and Use Cases** LLMs are characterized by their large-scale training data and parameter counts, allowing them to handle diverse tasks like text generation, classification, and even complex reasoning (e.g., chain-of-thought reasoning). They excel in few-shot or zero-shot learning scenarios, requiring little to no additional training data for specific applications.

- **Development and Tuning Tools** Google Cloud offers tools like Vertex AI Studio and Gemini for building, fine-tuning, and deploying LLMs. These tools enable developers to customize models for specific use cases, such as sentiment analysis or customer support, with minimal coding expertise. Parameter-efficient tuning methods (PETM) further optimize LLMs without altering the base model.


## Introduction to Responsible AI
- **Responsible AI Practices:** Responsible AI involves ensuring transparency, fairness, accountability, and privacy in AI systems. Organizations, including Google, develop their own AI principles to guide ethical decision-making throughout the AI lifecycle, from design to deployment, to avoid bias, harm, or unintended consequences.

- **Human-Centric AI Development:** AI systems are shaped by human decisions and values at every stage, from data collection to deployment. Responsible AI requires continuous evaluation to ensure ethical considerations are prioritized, building trust and ensuring AI benefits society while minimizing risks.

- **Google’s AI Principles:** Google’s seven AI principles focus on social benefit, avoiding bias, safety, accountability, privacy, scientific excellence, and responsible use. These principles guide product development and business decisions, ensuring AI aligns with ethical standards and avoids harmful applications like surveillance or weapons.

## Prompt Design in Vertex AI
### Lab 1 - Generative AI with Vertex AI: Prompt Design
In this lab, I learned prompt engineering best practices using Google’s Generative AI SDK. Key steps included setting up a Vertex AI Workbench notebook, applying concise and specific prompts, reducing output variability with system instructions, and improving response quality by including examples. I also explored text generation use cases like ideation, question answering, and classification, while following guidelines to minimize hallucinations and ensure task-specific outputs. This hands-on experience highlighted effective strategies for leveraging large language models (LLMs) in real-world applications.

### Lab 2 - Get Started with Vertex AI Studio
In this lab, I learned to analyze images and videos using Gemini in Vertex AI Studio's Freeform mode, extracting and generating information through well-designed prompts. I explored text prompt design techniques like zero-shot, one-shot, and few-shot prompting, adjusting parameters like temperature and token limits to influence model responses. Additionally, I created conversational prompts in Chat mode, experimenting with system instructions to guide the model's behavior. This hands-on experience deepened my understanding of multimodal AI capabilities and effective prompt engineering strategies.

### Lab 3 - Getting Started with the Gemini API in Vertex AI
In this lab, I learned to use the Gemini API in Vertex AI with the Vertex AI SDK for Python, focusing on the Gemini 1.5 Pro model. I generated text from text prompts, images, and videos, explored streaming responses, and adjusted safety filters to control content output. Additionally, I experimented with multimodal prompts, combining text and images, and analyzed publicly available web media. This hands-on experience equipped me with practical skills to integrate and leverage Gemini’s generative AI capabilities for diverse applications.

### Lab 4 - Prompt Design in Vertex AI: Challenge Lab
In this challenge lab, I applied my skills in Vertex AI to create tools for Cymbal Direct’s marketing campaign. I built a Gemini image analysis tool to generate evocative product descriptions and a tagline generator using Freeform prompts, customizing outputs based on product attributes and emotional resonance. I also explored and modified Python code for both tools in Jupyter Notebooks, refining prompts to produce creative and specific results. This hands-on experience deepened my understanding of prompt design and generative AI implementation in real-world scenarios.


## Responsible AI: Applying AI Principles with Google Cloud
### Introduction
- **Course Introduction:** In this course, I learned about the importance of responsible AI practices, focusing on transparency, fairness, accountability, and privacy. I also understood that human decisions and values are central to AI development, shaping how AI systems are designed, deployed, and maintained to ensure ethical and beneficial outcomes.
- **Google and responsible AI:** In this course, I learned that responsible AI is essential to address ethical concerns like fairness, bias, and accountability, ensuring AI benefits society without unintended harm. I also understood that building trust through transparent processes and fostering a collaborative culture are key to developing AI responsibly, regardless of an organization's size or resources.
- **An introduction to Google’s AI Principles:** In this course, I learned about Google’s seven AI principles, which guide ethical AI development:
    1. *Social Benefit:* AI should benefit society, with benefits outweighing risks.
    2. *Avoid Unfair Bias:* AI should avoid reinforcing biases related to sensitive characteristics like race, gender, or religion.
    3. *Safety:* AI must be built and tested to avoid unintended harm.
    4. *Accountability:* AI systems should allow for feedback, explanations, and appeals.
    5. *Privacy:* AI should incorporate privacy safeguards and provide transparency over data use.
    6. *Scientific Excellence:* AI development should uphold high scientific standards and share knowledge responsibly.
    7. *Responsible Use:* AI should be limited to applications that align with these principles, avoiding harmful or abusive uses.
    
    I also understood the importance of avoiding harmful AI applications, such as those involving surveillance or weapons, and how these principles serve as a foundation for responsible innovation and decision-making.

### The Business Case for Responsible AI
- **The Economist Intelligence Unit report:** From the insights shared, I learned that responsible AI is not only ethical but also a strategic advantage for businesses, driving long-term success and trust. A report by The Economist Intelligence Unit highlights how responsible AI enhances product quality, talent retention, data security, regulatory readiness, financial growth, stakeholder relationships, and brand trust. These insights demonstrate the business value of integrating responsible AI practices into organizational strategies.

- **The business case for responsible innovation:** The Economist Intelligence Unit’s report highlights seven key benefits of responsible AI:
    1. *Product Development:* Ethical AI reviews reduce risks, lower costs, and improve product quality by addressing bias and fostering trust.  
    2. *Talent Retention:* Companies with responsible AI practices attract and retain top talent, as employees value ethical commitments.  
    3. *Data Security:* Safeguarding data builds customer trust, reduces breach costs, and enhances AI outcomes through diverse datasets.  
    4. *Regulatory Readiness:* Proactive responsible AI practices prepare organizations for future regulations, reducing compliance risks.  
    5. *Revenue Growth:* Ethical AI boosts customer loyalty, vendor partnerships, and financial performance, with consumers willing to pay more for responsible products.  
    6. *Partnerships:* Investors increasingly favor companies prioritizing responsible AI, driving funding and long-term growth.  
    7. *Trust and Branding:* Responsible AI strengthens public trust, protects brand reputation, and mitigates risks of negative publicity.  

    These insights demonstrate how responsible AI not only aligns with ethical values but also drives business success and competitive advantage.

### AI’s Technical Considerations and Ethical Concerns
- **AI’s technical considerations and ethical concerns:**
- **Concerns about artificial intelligence**