s = "Python"
s = list(s)
s.reverse()
print(s)

final_string = "".join(s)
print(f"Moj ciag znakow to {final_string}")
path_to_file_windows = "C:\Repositories\codebrainers_2025_07"
path_to_file_linux = "C:/Repositories/codebrainers_2025_07"
print(path_to_file_windows, path_to_file_linux)
path_to_file_list = ("C:", "Repositories", "codebrainers_2025_07")
changed_pathL = "/".join(path_to_file_list)
changed_pathW = "\\".join(path_to_file_list)
print(f"Final path linux: {changed_pathL}")
print(f"Final path windows: {changed_pathW}")
