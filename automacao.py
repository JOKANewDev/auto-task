import pyautogui as joka
import time
import os

joka.PAUSE = 1

def motivacao():
    joka.alert("🚀 Bora estudar, Hoje é dia de vitória, ah e detalhe hein e detalhe, elas olham 👊")

def fechar_apps():
    apps = ["steam.exe", "wallpaper64.exe", "chrome.exe", "discord.exe"]
    for app in apps:
        os.system(f"taskkill /f /im {app}")

def abrir_estudo():
    joka.press('win')
    joka.write("Edge")
    joka.press('ENTER')
    time.sleep(2)

    sites = [
        "youtube.com",
        "https://www.cursoemvideo.com/meus-cursos/",
        "open.spotify.com",
        "https://pomofocus.io/"
    ]

    for site in sites:
        joka.write(site)
        joka.press('ENTER')
        time.sleep(2)
        joka.hotkey('ctrl', 't')

    # vai direto para a aba 2 (Curso em Vídeo)
    joka.hotkey('ctrl', '2')

def finalizar():
    joka.alert("✅ Ambiente pronto, foco total irmão!")

# ========================
# EXECUÇÃO DO SCRIPT
# ========================
if __name__ == "__main__":
    motivacao()
    fechar_apps()
    abrir_estudo()
    finalizar()
