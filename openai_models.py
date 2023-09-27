import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.organization = "org-YoC9IJpxWF2tZp9FpEI3nkVH"
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Model.list()
print(response)
