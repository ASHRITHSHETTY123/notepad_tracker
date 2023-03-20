import glob, os

os.chdir(r"C:\Users\ASHRITH SHETTY\Desktop\Notepad_Tracker\docs")
file_list = glob.glob("*.txt")
print(file_list)
