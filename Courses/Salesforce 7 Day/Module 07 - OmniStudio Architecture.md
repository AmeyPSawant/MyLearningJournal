# OmniStudio Architecture

## Meet OmniStudio

### Say Hello to OmniStudio

OmniStudio simplifies digital transformation with drag-and-drop tools for creating guided experiences without code.  
It integrates Salesforce automation capabilities and supports omnichannel service across devices.  
OmniStudio's layers include [Digital Experience](./Glossary.md#digital-experience-layer), [Service Management](./Glossary.md#service-management-layer), and [Developer Experience](./Glossary.md#developer-experience-layer).

## Explore the Digital Experience Layer

### Digital Experience Components and Capabilities

The Digital Experience layer in OmniStudio enhances user interactions with two main UI components: [FlexCards](./Glossary.md#flexcards) and [OmniScripts](./Glossary.md#omniscripts).  
These components, built on Salesforce Lightning Web Components (LWC), improve UI performance and create engaging user experiences.

### Salesforce Lightning Web Components

FlexCards and OmniScripts transform into Lightning Web Components when activated.  
These components work across communities, portals, and devices, ensuring a consistent multichannel experience.  
They can also interact with each other, like embedding FlexCards in OmniScripts for enhanced functionality.

## Use the Service Management Layer

### Control Data with the Service Management Layer

The Service Management layer in OmniStudio provides data services to read, write, transform, calculate, and track data both within and outside Salesforce.  
Key components include OmniStudio Data Mappers for data retrieval and transformation, and OmniStudio Integration Procedures for executing multiple actions in a single server call.

### Service Management Components and Capabilities

Data Mappers are tools for reading, transforming, and writing Salesforce data.  
There are four types: [Turbo Extract](./Glossary.md#data-mapper-turbo-extract), [Extract](./Glossary.md#data-mapper-extract), [Load](./Glossary.md#data-mapper-load), and [Transform](./Glossary.md#data-mapper-transform), each suited for specific data operations.  
Integration Procedures _handle data retrieval_, saving, and manipulation behind the scenes, offering _fast processing_ and _minimizing server-client interactions_.  
These components enhance development speed and reduce maintenance costs.
