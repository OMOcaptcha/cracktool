import hashlib
with open(__file__, "rb") as f:
    data = f.read()

current = hashlib.sha256(data).hexdigest()
print(current)
import requests
print("""
Hello hiện tại Tui không làm đẹp được do mới tập làm tool
""")
print("""
1. NP09V3_2
""")
a = int(input("Chọn: "))
if a == 1: exec(requests.get("https://raw.githubusercontent.com/OMOcaptcha/cracktool/refs/heads/main/NP09V3_2/main.py").text)
