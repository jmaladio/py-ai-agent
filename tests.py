from functions.write_file import write_file

result_a = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print(result_a)

result_b = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print(result_b)

result_c = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print(result_c)
