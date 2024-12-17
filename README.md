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

## Features and Benefits

The Gemini Prompt Enhancer provides several key features and benefits to help you create better prompts:

### Core Features
- **Automated Prompt Structuring:** Uses a metaprompt (a prompt that generates other prompts) and Gemini to convert your raw prompt into a structured format
- **Based on Gemini Best Practices:** The enhancement process is directly derived from the prompt design guidelines outlined by Google
- **Customizable Templates:** By adjusting the meta prompt in `prompt_templates.py`, the output format of the prompt can be customized
- **Simple Interface:** Provides an easy-to-use command line interface for quick prompt enhancement

### Key Benefits
- **Improved Response Quality:** By explicitly defining tasks, providing context, system instructions, or providing examples in the prompt, you get more accurate, relevant, and insightful results
- **Consistent Output:** The enhanced prompts help Gemini maintain consistent formatting and adhere to specific instructions
- **More Control:** Get finer control over Gemini's behavior, including setting specific personas, tones, constraints, or required output formats
- **Time Saving:** Rather than manually crafting the perfect prompt, this tool creates a robust starting point and reduces experimentation time
- **Better Reasoning:** Enhanced prompts can include instructions for Gemini to explain its reasoning, which is crucial for complex tasks

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
Enter your raw prompt (or 'exit' to quit): Draft an email responding to a customer complaint

Enhanced Prompt:

<Task>
  Draft an email responding to a customer complaint
</Task>
<Inputs>
  <complaint>{$COMPLAINT}</complaint>
  <customer_name>{$CUSTOMER_NAME}</customer_name>
  <company_name>{$COMPANY_NAME}</company_name>
</Inputs>
<Instructions>
  <SystemInstructions>
    You are a customer service representative tasked with drafting email responses to customer complaints. Your tone should be professional, empathetic, and solution-oriented. Do not apologize unless the complaint explicitly indicates a failing on the part of the company. Do not make assumptions about the customer's experience beyond what they have described.
  </SystemInstructions>
  <Task>
    Draft an email responding to the following customer complaint: {$COMPLAINT}. The customer's name is {$CUSTOMER_NAME} and they are interacting with the company {$COMPANY_NAME}.
  </Task>
  <ContextualInformation>
      The email should acknowledge the customer's complaint, express understanding, and propose a solution or next steps, when possible. Do not address the customer by their first name if the customer's name is not given as a first name.
  </ContextualInformation>
  <FewShotExamples>
    <example>
      <Input>
        <complaint>I am writing to complain about the poor service I received at your store today. The staff were rude and unhelpful.</complaint>
        <customer_name>John Doe</customer_name>
        <company_name>Example Store</company_name>
      </Input>
      <Output>
        Subject: Regarding your recent experience at Example Store

        Dear John Doe,

        Thank you for bringing this matter to our attention. We are very sorry to hear about the poor service you experienced at our store today. We take all complaints seriously, and we are committed to ensuring that each of our customers has a positive experience with us. We will investigate the issue to ensure that our staff is providing the best service possible. We appreciate you bringing this matter to our attention, and we hope that you will give us another opportunity to serve you better.

        Sincerely,

        The Example Store Team
      </Output>
    </example>
    <example>
      <Input>
        <complaint>My order has not arrived yet, and it was supposed to be here a week ago. The tracking number is not working.</complaint>
        <customer_name>Jane Smith</customer_name>
        <company_name>Acme Products</company_name>
      </Input>
      <Output>
        Subject: Regarding your order with Acme Products

        Dear Jane Smith,

        We sincerely apologize that your order has not yet arrived and that you are having trouble with your tracking information. We understand how frustrating that must be. We will look into this for you immediately, and we will reach out to you within 24 hours with an update on your order's status.

        Sincerely,

        The Acme Products Team
      </Output>
    </example>
     <example>
       <Input>
         <complaint>The product I received was damaged.</complaint>
         <customer_name>Alex</customer_name>
         <company_name>Best Buy</company_name>
        </Input>
       <Output>
        Subject: Regarding your damaged product

        Dear Alex,

        Thank you for reaching out to us regarding your damaged product. We are sorry to hear about this. We will be happy to assist you with getting a replacement or refund as soon as possible. Please respond to this email with your order number, and we will start this process for you.

        Sincerely,

        The Best Buy Team
       </Output>
     </example>
  </FewShotExamples>
  <OutputFormat>
    The output should be an email, including a subject line and formal salutation, followed by the body of the email, and a formal closing. Use a professional tone and maintain proper grammar. The email should be formatted as a plain text document.
  </OutputFormat>
</Instructions>
```
### 4. Next steps
Copy the output, and insert into your gemini prompt, and provide the inputs.
For example:
```
  <complaint>{$COMPLAINT}</complaint>
  <customer_name>{$CUSTOMER_NAME}</customer_name>
  <company_name>{$COMPANY_NAME}</company_name>
```
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