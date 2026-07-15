linux_commands = {
    "create file": "touch",
    "display file": "cat",
    "show file": "cat -n",
    "current directory": "pwd",
    "list files": "ls",
    "create directory": "mkdir",
    "remove file": "rm",
    "change directory": "cd"
}


def generate_commands(question):
    question = question.lower()

    commands = []

    for key, value in linux_commands.items():
        if key in question:
            commands.append(value)

    return list(set(commands))