import os
import base64
import requests
from dotenv import load_dotenv
from app.services.profile_analyzer import analyzer
from app.prompts.tasks import TEXT_PROMPT


load_dotenv()
# OpenAI API Key and API Route
API_KEY = os.getenv("OPENAI_API_KEY")
API_ROUTE = os.getenv("COMPLETION_API")

tick_start = "```"
tick_end = "```"

headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}


def image_post_service(uploaded_file):
    image_as_encoded = base64.b64encode(uploaded_file.read()).decode("utf-8")

    payload = {
        "model": "gpt-4-turbo",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": TEXT_PROMPT},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_as_encoded}"
                        },
                    },
                ],
            }
        ],
        "max_tokens": 500,
    }

    response = requests.post(API_ROUTE, headers=headers, json=payload)

    data = response.json()

    profile_description = data["choices"][0]["message"]["content"]

    formatted_description = tick_start + profile_description + tick_end

    return analyzer(formatted_description)
