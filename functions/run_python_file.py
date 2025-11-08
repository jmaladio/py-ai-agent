import os
import sys
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        abs_target_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

        if not (abs_target_path.startswith(abs_working_directory + os.sep)):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not (os.path.exists(abs_target_path)):
            return f'Error: File "{file_path}" not found.' 

        if not (abs_target_path[-3:] == '.py'):
            return f'Error: "{file_path}" is not a Python file.'

        completed_process = subprocess.run([sys.executable, file_path, *args], cwd=abs_working_directory, capture_output=True, text=True, timeout=30)
        if (completed_process.stdout == '' and completed_process.stderr == ''):
            return 'No output produced.'
        return f'STDOUT: {completed_process.stdout}\nSTDERR: {completed_process.stderr}{f'\nProcess exited with code {completed_process.returncode}' if completed_process.returncode != 0 else ''}'

    except Exception as e:
            return f'Error: executing Python file {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
