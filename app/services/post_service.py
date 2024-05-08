from dotenv import load_dotenv
import base64
import os
import requests

load_dotenv()
# OpenAI API Key
api_key = os.getenv('OPENAI_API_KEY')

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}


def image_post_service(uploaded_file):
    image_as_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
   
    payload = {
			"model": "gpt-4-turbo",
			"messages": [
				{
					"role": "user",
					"content": [
						{
							"type": "text",
							"text": "What’s in this image? Describe the appearance of the person. Analyze also if the image includes nudity or daring or provocative. Mentioned also if the image is in bad taste and not that pleasant."
						},
						{
							"type": "image_url",
							"image_url": {
								"url": f"data:image/jpeg;base64,{image_as_encoded}"
							}
						}
					]
				}
			],
			"max_tokens": 300
    }
   
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    
    data = response.json()
    
    return (data['choices'][0]['message']['content'])