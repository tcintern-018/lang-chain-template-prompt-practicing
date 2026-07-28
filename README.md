LangChain Prompt Template 

This project demonstrates the basics of LangChain by integrating an LLM chat model with a Prompt Template. In prompt_template.py, a LangChain chat model is used to process a structured prompt that asks the model to explain Machine Learning as if teaching a 10-year-old child. The project showcases how different prompt styles can guide the model to produce responses tailored to a specific audience and context.

now in below i mention some template you can try it by replacing it,

template = PromptTemplate.from_template(
    "Explain {topic} like I am 10 years old."
)

template = PromptTemplate.from_template(
    "Explain {topic} as a university professor."
)

template = PromptTemplate.from_template(
    "Give five bullet points about {topic}."
)
