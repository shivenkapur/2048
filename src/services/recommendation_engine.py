import os

from openai import OpenAI
from custom_types.board_values import BoardValues

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ['HUGGING_FACE_KEY'],
)

def ask_ai_for_recommendation(board_values: BoardValues) -> str:
    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct:cerebras",
        messages=[
            {
                "role": "system",
                "content": _get_prompt(board_values)
            }
        ],
        max_tokens=1
    )

    return completion.choices[0].message.content

def _get_prompt(board_values: BoardValues):
    prompt = f"You are a recommendatione engine for suggesting the next move in the game of 2048. Respond with ONLY one word: 'Left', 'Right', 'Up' or 'Down'. My current board is {board_values}."

    return prompt
