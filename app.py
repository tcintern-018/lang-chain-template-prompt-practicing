from config import llm
from prompt_template import (
    teacher_prompt,
    career_prompt,
    code_review_prompt,
)

choice = input(
    "Choose Assistant (teacher/career advisor/code reviewer): "
).lower()

user_input = input("Enter your question: ")

if choice == "teacher":
    chain = teacher_prompt | llm

elif choice == "career advisor":
    chain = career_prompt | llm

elif choice == "code reviewer":
    chain = code_review_prompt | llm

else:
    print("Invalid choice")
    exit()

response = chain.invoke(
    {
        "topic": user_input
    }
)

print(response.content)