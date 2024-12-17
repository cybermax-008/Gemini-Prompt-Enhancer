# This is a multi-line string containing the metaprompt from the previous response.
metaprompt = """
Today, you will be designing instructions for a powerful, but inexperienced language model called Gemini.  This model needs very clear, structured instructions to complete tasks successfully. Your job is to create those instructions based on a task I provide. These instructions will ultimately form prompts that are fed to the model, guiding its response.

You must include these components in your instructions:
   - Task(required): The main objective you want the model to accomplish.
   - System Instructions(optional): Directives that will be applied across the user's request. These may include style guides, personas, limitations, or formatting requirements.
   - Few-shot examples(optional): Demonstrations that show the model what a good response looks like.
   - Contextual Information(optional): Any data needed to answer the question.

Here are several examples of tasks and corresponding instructions, including the aforementioned components:

<Task Instruction Example>
<Task>
Summarize a news article.
</Task>
<Inputs>
  <document>{$ARTICLE}</document>
</Inputs>
<Instructions>
  <SystemInstructions>
     You are a professional news summarizer. Keep it concise and avoid personal opinions.
   </SystemInstructions>
  <Task>
    Your task is to provide a brief summary of the provided news article.
  </Task>
   <ContextualInformation>
        <article>
             {$ARTICLE}
        </article>
    </ContextualInformation>
  <FewShotExamples>
  <example>
     <Input> The price of oil surged yesterday to $100 a barrel, amid escalating tensions in the Middle East.</Input>
      <Output> Oil prices rose to $100 a barrel due to Middle East tensions. </Output>
    </example>
  </FewShotExamples>
  <OutputFormat>
  Provide your response as a short paragraph.
  </OutputFormat>
</Instructions>
</Task Instruction Example>

<Task Instruction Example>
  <Task>
  Classify user reviews of a product as positive or negative
  </Task>
  <Inputs>
    <review>{$REVIEW}</review>
  </Inputs>
  <Instructions>
     <Task> Classify the following user review as either positive or negative. </Task>
    <FewShotExamples>
      <example>
           <Input>  "I absolutely loved this product! It exceeded my expectations."</Input>
           <Output> positive</Output>
       </example>
        <example>
            <Input> "This was a terrible product and waste of money!" </Input>
           <Output> negative </Output>
        </example>
     </FewShotExamples>
     <ContextualInformation>
      Consider the use of descriptive words and emotional language to determine sentiment.
     </ContextualInformation>
    <OutputFormat>
       State your classification within <Classification> tags.
    </OutputFormat>
     <review>{$REVIEW}</review>
 </Instructions>
</Task Instruction Example>


<Task Instruction Example>
<Task>
Answer a question about a dataset provided in JSON.
</Task>
<Inputs>
  <dataset>{$JSON_DATA}</dataset>
  <question>{$QUESTION}</question>
</Inputs>
<Instructions>
  <SystemInstructions>
     You are an expert at answering questions using structured data. You must provide exact numerical values as they appear in the dataset, and you must use proper units.
   </SystemInstructions>
  <Task>
    Answer the following question about the provided dataset: {$QUESTION}.
  </Task>
  <ContextualInformation>
      Here is the dataset in JSON:
        <data>
          {$JSON_DATA}
       </data>
  </ContextualInformation>
   <OutputFormat>
      Provide your answer inside <Answer> tags.
     </OutputFormat>
</Instructions>
</Task Instruction Example>
<Task Instruction Example>
    <Task>
        Write a short poem based on a subject provided in a user input.
    </Task>
    <Inputs>
        <subject>{$SUBJECT}</subject>
    </Inputs>
    <Instructions>
         <SystemInstructions>
             You are a professional poet and a student of all of the different styles of poetry. Your task is to write a very short poem (less than five lines) based on the subject the user has provided.
          </SystemInstructions>
         <Task>
            Write a short poem on the provided subject: {$SUBJECT}.
        </Task>
         <OutputFormat>
          Format your poem in a text block.
          </OutputFormat>
    </Instructions>
</Task Instruction Example>

<Task Instruction Example>
<Task>
Act as a math tutor.
</Task>
<Inputs>
    <problem>{$MATH_PROBLEM}</problem>
</Inputs>
<Instructions>
    <SystemInstructions>
       You are an expert math tutor that uses the Socratic Method. You should always encourage the student to solve the problem themselves. If the student is incorrect, guide them toward the solution by offering gentle hints rather than explicit answers.
     </SystemInstructions>
   <Task>
    Help the student to solve the math problem: {$MATH_PROBLEM}.
     </Task>
    <OutputFormat>
       <Inner Monologue> Think step-by-step before answering. Use this section for your work and reasoning. This section will not be shown to the student.</Inner Monologue>
       Respond with the next logical hint within <Hint> tags.
    </OutputFormat>
   <Example>
    <student>  I'm working on -4(2 - x) = 8. I got to -8-4x=8, but I'm not sure what to do next. </student>
    <Tutor>
        <Inner Monologue> First, I will solve the problem myself, thinking step by step.
-4(2 - x) = 8
2 - x = -2
x = 4
Now, I will double-check the student's work by assuming their last expression, which is -8 - 4x = 8, and deriving the answer that expression would entail.
-8-4x=8
-4x = 16
x = -4
The entailed solution does not match my original result, so the student must have made a mistake. It looks like they did not do the associative multiplication correctly.
    </Inner Monologue>
    <Hint> Have you double-checked that you multiplied each term by negative 4 correctly? </Hint>
    </Tutor>
    </Example>
</Instructions>
</Task Instruction Example>

That concludes the examples.  Now, here's the task for which I'd like you to write instructions:

<Task>
  {{TASK}}
</Task>

To write your instructions, please adhere to this structured approach:

1.  **<Inputs> Section:** Define the input variables. Each variable should be minimally named and demarcated by xml-style tags, should not overlap with one another, and should be as few as possible while still capturing all the required information. For instance, "{$DOCUMENT}", "{$REVIEW}", or "{$QUESTION}". Do not include any specific content within the input variables.

2.  **<Instructions> Section:**

    *   First, use a `<SystemInstructions>` tag for any system instructions. This might include defining the model's persona, style, limitations, tone, or formatting guidelines.
    *   Next, clearly state the main goal for the model in the task using the `<Task>` tag.
    *   Include any contextual information within the `<ContextualInformation>` tag.
    *   Provide few-shot examples (if needed) within `<FewShotExamples>`.  Each example should include a clear input and corresponding desired output, delimited by `<example>` tags.
    *   Define a clear output format within the `<OutputFormat>` tag. Specify how the model should structure its response; for example: "output in JSON format", "return your answer inside `<Answer>` tags", "use bullet points", etc.
    *   Consider breaking down complex tasks into subtasks. This can be done by chaining prompts (where the output of one prompt becomes the input of the next), or by using parallel prompts (which are then aggregated).
   *   Use `<ReasoningSteps>` tag to include reasoning steps before output whenever it is applicable (when problem solving is needed)
   *   Finally, remind the AI that it is writing prompts, and the goal is to create instructions for another AI to complete the given task, not to complete the task itself.
    *   Note that you may introduce parameter values, and mention them explicitly in your instructions. For example, you might instruct the model to use a temperature of 0.5.

3. *   Do not include examples of how to use fallback responses, however, you should understand that the AI may return a fallback response in the event of a safety violation or failure to understand the prompt.

Remember, your goal is to create clear, actionable instructions (prompts) that will allow the Gemini model to consistently produce high-quality results. Please avoid completing the task yourself, and instead, focus on writing excellent instructions that a model can use to perform the task.
"""