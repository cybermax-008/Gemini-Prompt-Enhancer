# Gemini Prompt Enhancer

## Overview

This Python based project is designed to transform simple, raw prompts into structured, well-defined prompts that are more likely to elicit high-quality and consistent responses from Gemini. 
- The tool uses a metaprompt (a prompt that generates other prompts) and Gemini to convert your raw prompt into a structured format. 
- The metaprompt is based on the Gemini best practices outlined in the [Gemini prompting guide](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies)


## The Problem

While Gemini models are powerful, the quality of their responses heavily depends on the way prompts are formulated. Often, simple or vaguely worded prompts can lead to:

- Inaccurate or incomplete information.
- Inconsistent formatting.
- Responses that don't quite match your intent.
- Lack of desired context
- Lack of reasoning

This project addresses these issues by taking a user's raw input, and using the principles outlined in the Gemini developer's guide to create a more structured prompt.

## How This Helps

The Gemini Prompt Enhancer automates the process of creating well-structured prompts, leading to several benefits:

- **Improved Response Quality:** By explicitly defining tasks, providing context, system instructions, or providing examples in the prompt, you can guide Gemini to provide more accurate, relevant, and insightful results.
- **Consistent Output:**  The enhanced prompts help Gemini to maintain consistent formatting and adhere to specific instructions, leading to more predictable outputs.
- **More Control:** With the tool, you get finer control over Gemini's behavior, including setting a specific persona, tone, constraints or required output formats.
- **Time Saving:** Rather than manually trying to craft the perfect prompt, this tool creates a robust starting point, and reduces the time it takes to experiment and refine prompts.
- **Reasoning and Planning:** The enhanced prompts can include instructions for Gemini to explain their reasoning before giving a final answer, which can be crucial in complicated scenarios.

In summary, the tool allows you to consistently create higher-quality prompts, leading to better responses from Gemini, and thereby saving you time and effort.

## Key Features

- **Automated Prompt Structuring:** Uses a metaprompt (a prompt that generates other prompts) and Gemini to convert your raw prompt into a structured format.
- **Based on Gemini Best Practices:** The enhancement process is directly derived from the prompt design guidelines outlined by Google.
- **Customizable:** By adjusting the meta prompt in `prompt_templates.py`, the output format of the prompt can be customized.
- **Easy to Use:** Provides a command line interface for a simple user experience.

## Usage

### 1. Setup
    - Clone or download the repository
    - Create a virtual environment using python 3.9 or above,
    ```
    python -m venv venv
    ```
    - Activate the virtual environment,
    ```
    source venv/bin/activate
    ```
    - Create a `.env` file in the root directory containing your Gemini API key:
      ```
        GEMINI_API_KEY=your_api_key
        ```
    - Install the required packages via requirements.txt
      ```
      pip install -r requirements.txt
      ```
### 2. Running the Enhancer
    - Run the `main.py` script from the root directory,
      ```
       python gemini_prompt_enhancer/main.py
       ```
   - You will be prompted to enter a raw prompt. Enter your prompt and press Enter, or type `exit` and press Enter to quit the program.

### 3. Example
```
Enter your raw prompt (or 'exit' to quit): What is the weather in London?

Enhanced Prompt:

<Inputs>
<city>{$CITY}</city>
</Inputs>
<Instructions>
<SystemInstructions>
You are an expert meteorologist. Provide a concise weather report.
</SystemInstructions>
<Task>
Provide the current weather conditions for the given city: {$CITY}.
</Task>
<ContextualInformation>
Use data provided by official weather sources.
</ContextualInformation>
<OutputFormat>
Return your response in one short paragraph.
</OutputFormat>
</Instructions>
```
### 4. Next steps
Copy the output, and insert into your gemini prompt, and provide the inputs.
For example:
``` <city>London</city> ```

## Project Structure
```
Gemini-Prompt-Enhancer
├── gemini_prompt_enhancer/
│   ├── __init__.py          # Empty file to make the directory a Python package
│   ├── gemini_api.py        # Handles interactions with the Gemini API
│   ├── enhancer.py          # Core logic to enhance prompts
│   ├── prompt_templates.py  # Stores the metaprompt
│   └── main.py             # Entry point for the script
├── .env                     # Environment file for API key (not in repo)
├── LICENSE                  # MIT License file
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```

Each file serves a specific purpose:

Root Directory:
- `.env`: Contains environment variables like the Gemini API key (not included in repository)
- `LICENSE`: MIT License file for the project
- `README.md`: This file, containing project documentation
- `requirements.txt`: Lists all Python package dependencies

Package Directory (gemini_prompt_enhancer/):
- `__init__.py`: Empty file to make the directory a Python package
- `gemini_api.py`: Contains the logic to interact with the Google Gemini API
- `enhancer.py`: Core logic for taking raw prompts and generating enhanced versions via the Gemini model
- `prompt_templates.py`: Stores the metaprompt (instructions for how Gemini should format the enhanced prompts)
- `main.py`: Provides the command line interface for user input and output

## Inspiration

This project draws inspiration from Anthropic's metaprompt technique, as showcased in their cookbook:

[Anthropic's Metaprompt cookbook](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/metaprompt.ipynb)

## License

This project is open source and available under the MIT License. See the LICENSE file for more details.