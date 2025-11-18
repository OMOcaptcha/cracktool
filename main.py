import os
os.system('cls' if os.name == 'nt' else 'clear')    
import requests
print("""
Hello hiện tại Tui không làm đẹp được do mới tập làm tool
""")
print("""
1. NP09V3_2
2. KTool
""")
a = int(input("Chọn: "))
if a == 1: exec(requests.get("https://raw.githubusercontent.com/OMOcaptcha/cracktool/refs/heads/main/NP09V3_2/main.py").text)
if a == 2: exec(requests.get("https://raw.githubusercontent.com/OMOcaptcha/cracktool/refs/heads/main/KTool/main.py").text)
