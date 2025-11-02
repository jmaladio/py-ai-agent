import os

def write_file(working_directory, file_path, content):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_target_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

        if not (abs_target_path == abs_working_directory or abs_target_path.startswith(abs_working_directory + os.sep)):
            return f'Error: Cannot write to "{abs_target_path}" as it is outside the permitted working directory'

        if not (os.path.exists(abs_target_path)):
            os.makedirs(abs_target_path)
            with open(abs_target_path, "w") as f:
                f.write(content)

            return f'Successfully wrote to "{file_path} ({len(content)} characters written)"'

    except Exception as e:
        raise f'Error: {e}'
