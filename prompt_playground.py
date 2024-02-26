from openai import AsyncOpenAI
import os

from chainlit.playground.providers import ChatOpenAI
import chainlit as cl

os.environ["HTTP_PROXY"] = "http://127.0.0.1:1087"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:1087"

client = AsyncOpenAI()

template = "Hello, {name}!"
variables = {"name": "John"}

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    # ... more settings
}


@cl.step(type="llm")
async def call_llm():
    generation = cl.ChatGeneration(
        provider=ChatOpenAI.id,
        variables=variables,
        settings=settings,
        messages=[
            {
                "content": template.format(**variables),
                "role":"user"
            },
        ],
    )

    # Make the call to OpenAI
    response = await client.chat.completions.create(
        messages=generation.messages, **settings
    )

    generation.message_completion = {
        "content": response.choices[0].message.content,
        "role": "assistant"
    }

    # Add the generation to the current step
    cl.context.current_step.generation = generation

    return generation.message_completion["content"]


@cl.on_chat_start
async def start():
    await call_llm()
