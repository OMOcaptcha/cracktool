import os
import sys
import time
import requests
from datetime import datetime

# Install libraries nếu chưa có
try:
    from colorama import init, Fore
    from rich.console import Console
    from rich.tree import Tree
    from rich.panel import Panel
    from rich.align import Align
    from rich.text import Text
except ImportError:
    os.system('pip install colorama rich requests')
    from colorama import init, Fore
    from rich.console import Console
    from rich.tree import Tree
    from rich.panel import Panel
    from rich.align import Align
    from rich.text import Text

# init colorama
init(autoreset=True)

console = Console()

# ============================
# CONFIG TOOL
# ============================

TOOL_TREE = {
    'cracktool': {
        'name': 'Crack Tool 100% hoạt động',
        'icon': '>>',
        'color': 'cyan',
        'tools': {
            '1.1': {'name': 'NP09V3_2', 'desc': 'Tool của Phạm Nhật'},
            '1.2': {'name': 'Review tool247', 'desc': 'Tool của Duy Khánh'},
        }
    },

    'golike': {
        'name': 'Crack Tool nhưng lười crack full',
        'icon': '>>',
        'color': 'cyan',
        'tools': {
            '2.1': {'name': 'bypass link4m', 'desc': 'của KTool'}
        }
    }
}


# ============================
# UI FUNCTIONS
# ============================

def show_header():
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%d/%m/%Y')
    console.print(Align.center(Text(f"Ngày: {current_date}  |  Giờ: {current_time}", style="dim italic")))
    console.print()

def create_tool_tree():
    tree = Tree('[bold magenta]MENU TOOL[/bold magenta]')
    for platform_key, platform_data in TOOL_TREE.items():
        branch = tree.add(
            f"[{platform_data['color']} bold]{platform_data['icon']} {platform_data['name']}[/{platform_data['color']} bold]"
        )
        for tool_id, tool_info in platform_data['tools'].items():
            branch.add(
                f"[white][{tool_id}][/white] "
                f"[{platform_data['color']}]{tool_info['name']}[/{platform_data['color']}] "
                f"[dim]- {tool_info['desc']}[/dim]"
            )
    return tree

def show_menu():
    panel = Panel(create_tool_tree(), title='[bold]TOOL Gộp crack của hải[/bold]', border_style='bright_blue')
    console.print(panel)

def show_footer():
    console.print(Panel(Align.center(Text(" ")), border_style='dim'))

# ============================
# EXEC TOOL
# ============================

def exec_tool(link):
    if not link:
        print(Fore.LIGHTRED_EX + 'Hiện tại chưa thể dùng tool này.')
        time.sleep(2)
        return

    try:
        res = requests.get(link).text
        exec(res, globals())
    except Exception as e:
        print(Fore.LIGHTRED_EX + f'Lỗi khi chạy tool: {e}')
        time.sleep(3)

# ============================
# MAIN
# ============================

def main():
    json_tool = {
        "1.1": 'https://raw.githubusercontent.com/OMOcaptcha/cracktool/refs/heads/main/NP09V3_2/main.py',
        "1.2": 'https://raw.githubusercontent.com/OMOcaptcha/cracktool/refs/heads/main/RVTOOL/obf-keykhan.py',
        "2.1": 'https://raw.githubusercontent.com/OMOcaptcha/cracktool/refs/heads/main/KTool/main.py',
    }

    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            show_header()
            show_menu()
            show_footer()

            console.print('[yellow]Nếu gặp lỗi "No module", hãy chạy: pip install <tên module>[/yellow]')
            choice = console.input('\n[bold cyan]=> Nhập lựa chọn: [/bold cyan]').strip()

            exec_tool(json_tool.get(choice))
            break

        except KeyboardInterrupt:
            console.print('[yellow]Đã dừng chương trình.[/yellow]')
            break


if __name__ == "__main__":
    main()
