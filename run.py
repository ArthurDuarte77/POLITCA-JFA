from datetime import datetime
import schedule
import time
import subprocess
from selenium.webdriver.common.keys import Keys
from collections import defaultdict
import docx
import time
import subprocess
import threading
import subprocess
import os
import time
from tqdm import tqdm
import shutil
import json
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from selenium.common.exceptions import *
import re
import pygetwindow as gw
import pyautogui
import time

# Tenta encontrar a janela do WhatsApp
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

    # Digita o texto desejado
    pyautogui.typewrite('politica E-commerce JFA')
    time.sleep(1)
    # Pressiona Tab e Enter
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
else:
    print("Janela do WhatsApp não encontrada.")

def extrair_informacoes_por_loja(caminho_arquivo):
    # Carrega o documento Word
    doc = docx.Document(caminho_arquivo)
    
    # Dicionário para armazenar informações por loja
    lojas = defaultdict(list)
    loja_atual = None
    
    # Itera sobre os parágrafos do documento
    for paragrafo in doc.paragraphs:
        texto = paragrafo.text.strip()
        if texto:
            # Verifica se o texto é um nome de loja
            if texto.startswith("*") and texto.endswith("*"):
                loja_atual = texto.strip("*")
            elif loja_atual:
                # Adiciona o texto à lista da loja atual
                lojas[loja_atual].append(texto)
    
    return lojas

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Bom dia!"
    elif 12 <= current_hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"


def enviar():
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
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('del')

        # Digita o texto desejado
        pyautogui.typewrite('politica E-commerce JFA')
        time.sleep(1)
        # Pressiona Tab e Enter
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
    else:
        print("Janela do WhatsApp não encontrada.")
    caminho_arquivo = 'dados_extraidos.docx'  # Substitua pelo caminho do seu arquivo Word
    lojas = extrair_informacoes_por_loja(caminho_arquivo)
    
    greeting = get_greeting()
    pyautogui.typewrite(greeting)
    pyautogui.press('enter')
    pyautogui.write("Seguem anúncios fora da política:")
    time.sleep(1)
    pyautogui.press('enter')
    for loja, detalhes in lojas.items():
        pyautogui.write(f"*{loja}*")
        time.sleep(1)
        for detalhe in detalhes:
            pyautogui.write(f"{detalhe}")
            time.sleep(1)   
        pyautogui.press('enter')
        
def executar_codigo():
    subprocess.run(['python', 'run_all.py'])
    enviar()

# Agendar a execução nos horários especificados
schedule.every().day.at("14:22").do(executar_codigo)
schedule.every().day.at("11:00").do(executar_codigo)
schedule.every().day.at("14:30").do(executar_codigo)
schedule.every().day.at("16:00").do(executar_codigo)
schedule.every().day.at("20:00").do(executar_codigo)
schedule.every().day.at("00:00").do(executar_codigo)

while True:
    schedule.run_pending()
    time.sleep(60) 