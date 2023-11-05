def exec_write_to_file(filename: str, content: str) -> str:
    with open(filename, 'w') as f:
        f.write(content)
    return "file created successfully"


def exec_read_from_file(filename: str) -> str:
    with open(filename, 'r') as f:
        contents = f.read()
    return contents


def exec_create_directory(directory_path: str) -> str:
    import os
    path = directory_path
    if not os.path.exists(directory_path):
        path = os.makedirs(directory_path)
    return path
