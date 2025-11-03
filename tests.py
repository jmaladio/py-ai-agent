from functions.run_python_file import run_python_file

result_a = run_python_file("calculator", "main.py")
print(result_a)

result_b = run_python_file("calculator", "main.py", ["3 + 5"])
print(result_b)

result_c = run_python_file("calculator", "tests.py")
print(result_c)

result_d = run_python_file("calculator", "../main.py")
print(result_d)

result_e = run_python_file("calculator", "nonexistent.py")
print(result_e)

result_f = run_python_file("calculator", "lorem.txt")
print(result_f)
