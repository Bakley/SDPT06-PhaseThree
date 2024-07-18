def load_sql_commands(file_path):
    with open(file_path, 'r') as file:
        commands = file.read().split(';')
    return [cmd.strip() for cmd in commands if cmd.strip()]

def get_commands(name, commands):
    for command in commands:
        if command.startswith(name):
            return command[len(name):].strip()
    return None
