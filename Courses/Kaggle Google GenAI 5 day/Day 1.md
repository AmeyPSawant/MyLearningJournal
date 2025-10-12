# Day 1 - Prompting & Evaluation

## Prompting

### Starter Code

Signed up on Google AI Studio for getting API Key.
Code Template for getting started in Python

```
# 1. Import and set up
from google import genai
from google.api_core import retry
import os

# 2. Add your API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or "your_api_key_here"
client = genai.Client(api_key=GOOGLE_API_KEY)

# 3. Add retry logic for rate limits
genai.models.Models.generate_content = retry.Retry(
    predicate=lambda e: isinstance(e, genai.errors.APIError) and e.code in {429, 503}
)(genai.models.Models.generate_content)

print("✅ GenAI client ready to use!")
```

### Generate Text with Gemini 2.0

```
client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain AI to me like I'm a kid.")

print(response.text)
```

### History parameter

Adding the history parameter enables the user to retrieve data.

```
chat = client.chats.create(model='gemini-2.0-flash', history=[])
response = chat.send_message('Hello! My name is Zlork.')
print(response.text)
```

### Model Details

```
from pprint import pprint

for model in client.models.list():
  if model.name == 'models/gemini-2.0-flash':
    pprint(model.to_json_dict())
    break
{'description': 'Gemini 2.0 Flash',
 'display_name': 'Gemini 2.0 Flash',
 'input_token_limit': 1048576,
 'name': 'models/gemini-2.0-flash',
 'output_token_limit': 8192,
 'supported_actions': ['generateContent',
                       'countTokens',
                       'createCachedContent',
                       'batchGenerateContent'],
 'tuned_model_info': {},
 'version': '2.0'}
```

### Controlling diversity of model

- Temperature

  - Higher temperature means more randomness.
  - Lower temperature means less randomness.

- Top-P

  - If Top_p is set to a lower value then less randomness.
  - If Top_p is set to a higher value then more randomness.
