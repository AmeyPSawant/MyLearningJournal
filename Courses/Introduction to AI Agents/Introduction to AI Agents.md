# Introduction to AI Agents

## What is an AI Agent
**To understand what are AI Agents we first have to understand what is not an AI Agent?**
Zero-shot / One-shot prompting
*For e.g. Write an essay in one go (which gives a static, non-adaptive responses)*

**An AI Agent is a system that**
- **Breaks tasks into steps** (e.g., research → draft → revise)
- **Iterates** to improve outputs (circular process vs. linear workflows)
- **Uses tools** (web search, code execution, etc.)


## Key Agentic Design Patterns
- **Reflection**: AI reviews/critiques its own output (e.g., code review)
- **Tool Use**: AI leverages external tools (web search, calculators, APIs)
- **Planning & Reasoning**: AI decomposes tasks into steps (e.g., image generation → voice description)
- **Multi-Agent Systems**: Specialized agents collaborate (like a human team)


## Multi-Agent Architectures
For understanding multi-agent architecture, we firs need to understand what does an agent consist of  
### Building Blocks of an Agent
- **TASK**: Goal (e.g., "Plan a 3-day Tokyo trip").
- **ANSWER**: Output format (e.g., itinerary with costs).
- **MODEL**: LLM (e.g., Claude, GPT-4).
- **TOOLS**: APIs, databases, etc. (e.g., Google Maps, Booking.com).

### Multi-Agent Design Patterns
| Pattern       | Description                                                                 | Example Use Case                          |
|---------------|-----------------------------------------------------------------------------|-------------------------------------------|
| **Sequential**   | Agents pass tasks linearly (assembly line).                                 | Document → Summary → Action Items → DB.  |
| **Hierarchical** | Manager agent delegates to sub-agents (e.g., market trends + sentiment analysis). | Business decision-making reports.        |
| **Hybrid**       | Combines sequential + hierarchical (e.g., autonomous vehicles).              | Real-time navigation + collision avoidance. |
| **Parallel**     | Agents process tasks simultaneously.                                        | Large-scale data analysis.                |
| **Asynchronous** | Agents act independently/at different times.                                | Cybersecurity threat detection.           |