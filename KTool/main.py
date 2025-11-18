import os
os.system('cls' if os.name == 'nt' else 'clear')    
import requests
exec(requests.get("https://raw.githubusercontent.com/OMOcaptcha/cracktool/refs/heads/main/KTool/taokey.py").text)
import requests

url = "https://raw.githubusercontent.com/OMOcaptcha/cracktool/refs/heads/main/KTool/KTool.py"
save_path = "KTool.py"

try:
    r = requests.get(url)
    r.raise_for_status()  # báo lỗi nếu request fail

    with open(save_path, "w", encoding="utf-8") as f:
        f.write(r.text)

except Exception as e:
    print("Lỗi khi tải:", e)
os.system("python KTool.py")
