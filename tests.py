from functions.get_file_content import get_file_content

result_a = get_file_content("calculator", "lorem.txt")
print(result_a)

result_b = get_file_content("calculator", "main.py")
print(result_b)

result_c = get_file_content("calculator", "pkg/calculator.py")
print(result_c)

result_d = get_file_content("calculator", "/bin/cat")
print(result_d)

result_e = get_file_content("calculator", "pkg/does_not_exist.py")
print(result_e)
