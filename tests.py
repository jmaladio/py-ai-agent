from functions.get_files_info import get_files_info

result_a = get_files_info("calculator", ".")
print(result_a)

result_b = get_files_info("calculator", "pkg")
print(result_b)

result_c = get_files_info("calculator", "/bin")
print(result_c)

result_d = get_files_info("calculator", "../")
print(result_d)

