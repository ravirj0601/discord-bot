
COMMAND_LIST = ["hello",
                "hi",
                "login",
                "logout"
                ]

def get_response(message):
    command = message.content[1:]

    if command not in COMMAND_LIST:
        raise ValueError(f"{command} action does not exist")

    if command == "hello":
        return f"Hello {message.author.display_name}!"

    if command == "hi":
        return f"Hi {message.author.display_name}!"
