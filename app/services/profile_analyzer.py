from openai import OpenAI
from dotenv import load_dotenv
from app.prompts.tasks import ANALYZER_PROMPT
import os

load_dotenv()

client = OpenAI()


def analyzer(profile_desc):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": ANALYZER_PROMPT},
            {"role": "assistant", "content": profile_desc},
        ],
    )
    return response.choices[0].message.content
