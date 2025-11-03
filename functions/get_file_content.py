import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_target_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

        if not (abs_target_path == abs_working_directory or abs_target_path.startswith(abs_working_directory + os.sep)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not (os.path.isfile(abs_target_path)):
            return f'Error: File not found or is not a regular file: "{file_path}"'


        with open(abs_target_path, "r") as f:
            file_size_bytes = os.path.getsize(abs_target_path)
            file_content_string = ''
            if (file_size_bytes > MAX_CHARS):
                file_content_string = f.read(MAX_CHARS) + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            else:
                file_content_string = f.read()

            return file_content_string

    except Exception as e:
        return f'Error: {e}'
