import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        wdir_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath(os.path.join(wdir_abs, directory))
    
        if not (target_abs == wdir_abs or target_abs.startswith(wdir_abs + os.sep)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_abs):
            return f'Error: "{directory}" is not a directory'

        dir_content = os.listdir(target_abs)
        dir_ls = list()
        for item in dir_content:
            item_path = os.path.abspath(os.path.join(target_abs, item)) 
            size = os.path.getsize(item_path)
            isDir = os.path.isdir(item_path)
            dir_ls.append(f"- {item}: file_size={size} bytes, is_dir={isDir}")

        initial_str = "Result for current directory:\n" if directory == "." else f"Result for '{directory}' directory:\n"
        result_str = "\n".join(dir_ls)
        return initial_str + result_str
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
