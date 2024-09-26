from lxml import html
from collections import defaultdict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from datetime import datetime
import pygetwindow as gw
import pyautogui
import time
import re
import json
import requests
import pandas
from tqdm import tqdm


def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Bom dia!"
    elif 12 <= current_hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def enviar(grouped_by_seller):
    whatsapp_window = None
    for window in gw.getAllTitles():
        if 'WhatsApp' in window:
            whatsapp_window = gw.getWindowsWithTitle(window)[0]
            break

    # Se a janela foi encontrada, traz para o foco
    if whatsapp_window is not None:
        whatsapp_window.activate()
        time.sleep(1)  # Espera um pouco para garantir que a janela está em foco

        # Pressiona Ctrl+F para abrir a busca
        pyautogui.hotkey('ctrl', 'f')
        # pyautogui.hotkey('ctrl', 'a')
        # pyautogui.press('del')

        # Digita o texto desejado
        pyautogui.typewrite('voce')
        time.sleep(1)
        # Pressiona Tab e Enter
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
    else:
        print("Janela do WhatsApp não encontrada.")
        return
    pyautogui.write(get_greeting())
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write("Segue anúncios fora da política")
    time.sleep(1)
    pyautogui.press('enter')


enviar("teste")