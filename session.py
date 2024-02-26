from typing import Optional, Dict

import chainlit as cl


@cl.on_chat_start
def on_chat_start():
    cl.user_session.set("counter", 0)


@cl.on_message
async def on_message(message: cl.Message):
    counter = cl.user_session.get("counter")
    counter += 1
    cl.user_session.set("counter", counter)

    await cl.Message(content=f"You sent {counter} message(s)!").send()


@cl.on_chat_start
async def start():
    image = cl.Image(path="/Users/Qing/Downloads/dbs.JPG", name="image1", display="inline")

    # Attach the image to the message
    await cl.Message(
        content="This message has an image!",
        elements=[image],
    ).send()


@cl.oauth_callback
def oauth_callback(
  provider_id: str,
  token: str,
  raw_user_data: Dict[str, str],
  default_user: cl.User,
) -> Optional[cl.User]:
  return default_user
