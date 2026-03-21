from sweetchgui import *
import os
import sys
import shutil
import subprocess
import threading

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

def sl(command):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW if hasattr(subprocess, 'CREATE_NO_WINDOW') else 0
        )
        return result.stdout
    except:
        return ""

#-------------------------------
temp = os.getenv('USERPROFILE')
temp2 = os.getenv('APPDATA')
#-------------------------------

#---------------------------------------------------------------------------------------------------
drfold = os.path.join(temp, "Desktop", "CosmicFixer")
dr1 = "https://aka.ms/vc14/vc_redist.x64.exe"
dr2 = "https://go.microsoft.com/fwlink/?linkid=2124701"
dr3 = "https://builds.dotnet.microsoft.com/dotnet/Sdk/7.0.410/dotnet-sdk-7.0.410-win-x64.exe"
dr4 = "https://builds.dotnet.microsoft.com/dotnet/Sdk/8.0.418/dotnet-sdk-8.0.418-win-x64.exe"
dr5 = "https://builds.dotnet.microsoft.com/dotnet/Sdk/9.0.311/dotnet-sdk-9.0.311-win-x64.exe"
dr6 = "https://builds.dotnet.microsoft.com/dotnet/Sdk/10.0.103/dotnet-sdk-10.0.103-win-x64.exe" 
#---------------------------------------------------------------------------------------------------

cat = "C:\\Sk3dGuardNew"
cat2 = os.path.join(temp2, "Sk3dGuard")
path = os.getenv('TEMP')

def invite():
    sl(f'start "" "https://discord.gg/nR4bVQW4"')

def create():
    if os.path.exists(drfold):
        shutil.rmtree(drfold)
    os.makedirs(drfold)
    window.debug.write("создал папку на рабочем столе")
    window.l.set_text('создал папку на рабочем столе')

def catlavan():
    window.debug.write("очищаю котлаван...")
    window.l.set_text('очищаю котлаван...')
    if os.path.exists(cat):
        shutil.rmtree(cat)
    if os.path.exists(cat2):
        shutil.rmtree(cat2)

def cleantemp():
    try:
        shutil.rmtree(path)
    except:
        window.debug.write("не смог очистить темп, нужны права администратора")

def download():
    window.debug.write("установка зависимостей...")
    window.l.set_text('установка зависимостей...')
    sl(f'curl -L -k -o "{drfold}\\Drive1.exe" "{dr1}"')
    window.debug.write("установил первый драйвер")
    sl(f'curl -L -k -o "{drfold}\\Drive2.exe" "{dr2}"')
    window.debug.write("установил второй драйвер")
    sl(f'curl -L -k -o "{drfold}\\Drive3.exe" "{dr3}"')
    window.debug.write("установил третий драйвер")
    sl(f'curl -L -k -o "{drfold}\\Drive4.exe" "{dr4}"')
    window.debug.write("установил четвертый драйвер")
    sl(f'curl -L -k -o "{drfold}\\Drive5.exe" "{dr5}"')
    window.debug.write("установил пятый драйвер")
    sl(f'curl -L -k -o "{drfold}\\Drive6.exe" "{dr6}"')
    window.debug.write("установил шестой драйвер")

def run():
    window.debug.write("открываю...")
    window.l.set_text('открываю...')
    sl(f"start \"\" \"{drfold}\\Drive1.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive2.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive3.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive4.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive5.exe\"")
    sl(f"start \"\" \"{drfold}\\Drive6.exe\"")

def runsc():
    try:
        create()
        catlavan()
        cleantemp()
        download()
        window.debug.write("установил драйвера")
        run()
        window.debug.write("успешно!")
        window.l.set_text('успешно исправил!')
        window.l3.unblock()
    except:
        print('ошибка!')

def start():
    window.l3.block()
    th = threading.Thread(target=runsc, daemon=True)
    th.start()

window = sgui(
    l1 = text('The Best open-source Fixer'),
    l2 = text('после исправления ваши конфиги удалятся!'),
    l3 = bigbutton('исправить котлаван'),
    l4 = text('beta v1.1.5'),
    l = status_bar('нажми на кнопку...'),
    debug = debug('=== дебаг ===\n'),
    theme = "midnight",
    title = f"::: Cosmo-Fixer :::",
    width = 500,
    height = 400,
    fade_in = 500,
    fade_out = 500
)

window.l3.on_click = start

invite()

icon_path = resource_path("icon.ico")
window.root.iconbitmap(icon_path)
window.start()