import chainlit as cl


# @cl.on_message
# async def main(message: cl.Message):
#     # Your custom logic goes here...
#
#     # Send a response back to the user
#     await cl.Message(
#         content=f"Received: {message.content}",
#     ).send()


@cl.password_auth_callback
def auth_callback(username: str, password: str):
    # Fetch the user matching username from your database
    # and compare the hashed password with the value stored in the database
    if (username, password) == ("admin", "admin"):
        return cl.User(
            identifier="admin", metadata={"role": "admin", "provider": "credentials"}
        )
    else:
        return None


@cl.on_message
async def on_message(message: cl.Message):
    tool_res = await tool()

    await cl.Message(content="This is the final answer").send()


@cl.step
async def tool():
    await cl.sleep(2)
    return "Response from the tool!"


@cl.on_chat_start
async def on_chat_start():
    print("Hello", cl.user_session.get("id"))
    # msg = cl.Message(content="")
    # for token in ["the", "quick", "brown", "fox"]:
    #     await msg.stream_token(token)

    # await msg.send()


@cl.on_stop
def on_stop():
    print("The user wants to stop the task!")


