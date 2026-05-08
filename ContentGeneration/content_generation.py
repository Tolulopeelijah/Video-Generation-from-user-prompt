from groq import Groq
from dataclasses import dataclass
from enum import Enum


class Difficulty(Enum):
    BEGINNER = "explain like I am completely new to this domain and have very basic knowledge beforehand"
    INTERMEDIATE = "I am convenient with some prerequisite knowledge, but not strong enough knowledge about the topic"
    ADVANCED = "I have some limited knowledge about the subject topic already, I only need more clarification and better understanding"


class PromptType(Enum):
    EXPLANATION = "EXPLANATION" # explaining a topic
    QUESTION = "QUESTION" # asking a question
    

@dataclass
class PromptConfig:
    difficulty: Difficulty
    num_tokens: int
    prompt_type: PromptType
    content: str


client = Groq()


SYSTEMS_PROMPT = """You are an expert at devloping course content that explains a topic or answer questions in a way that match a given difficulty level
                    the course content will be used to prepare a top tier animation video, reading through the content, the user should comprehend fully 
                    everything necessary to know about the subject topic.
                    feel free to make use of available tools when you can't don't have enough knowledge about any concept.
                    if any assumption is made about any prerequisite knowledge, state it in the content, and if it won't take much time and space, display 
                    some knowledge that will be needed to understand the subject topic.

                    your content must not be abusive, offensive or insultive
                    do not claim to know anything you are not sure of and connot back up with references
                    """

def generate_content(prompt: str) -> str:



    difficulty, time_range, prompt_type, content = prompt

    if prompt_type == 'topic':
        USER_CONTENT = f"in the time range of {PromptConfig.time_} explain {PromptConfig.content} with a difficulty level of {PromptConfig.difficulty}"

    elif prompt_type == 'question':
        USER_CONTENT = f"in the time range of {time_range}, {content}. (answer with a difficulty level of {difficulty})"

    else:
        raise NameError(f"{prompt_type} not recognized")


    messages = [

        {
            "role": "user",
            "content": SYSTEMS_PROMPT
        },


        {
            "role": "user",
            "content": USER_CONTENT
        }
    ],

    model = model
    completion = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile", 
        temperature=0.7,
        top_p=1
    )
    return completions[0].message.content)








time range
difficulty
rag, online_search and other tool use  
