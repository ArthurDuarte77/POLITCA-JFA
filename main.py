import requests
import keyboard
from lxml import html
from collections import defaultdict
from datetime import datetime
import schedule
import time
import subprocess
import requests
import pandas
from tqdm import tqdm

start_row = 20  
end_row = 33
num_rows = end_row - start_row

db = pandas.read_excel("politica-promo.xlsx", engine='openpyxl')

db.columns = ['PRODUTO', 'SITE', 'COLUNA3', 'CLÁSSICO ML', 'COLUNA5', 'PREMIUM ML', 'COLUNA7', 'MARKETPLACES', 'COLUNA9']

df = pandas.read_excel("GESTÃO DE AÇÕES E-COMMERCE.xlsx", usecols='C:O', skiprows=start_row, nrows=num_rows, engine='openpyxl', sheet_name="POLÍTICA COMERCIAL Out24 II")

df.columns = ['PRODUTO', 'inutil1', 'SITE', 'COLUNA3','inutil2', 'CLÁSSICO ML', 'COLUNA5','inutil3', 'PREMIUM ML', 'COLUNA7','inutil4', 'MARKETPLACES', 'COLUNA9']

for index, i in df.iterrows():
    if i['PRODUTO'] == "FONTE 40A":
        fonte40Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte40Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte40Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte40PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte40ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte40Marketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 60A":
        fonte60Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte60Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte60Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte60PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte60ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte60Marketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 60A LITE":
        fonte60liteMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte60liteClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte60litePremium = round(i['COLUNA7'], 2) - 0.01;
        fonte60litePremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte60liteClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte60liteMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 70A":
        fonte70Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte70Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte70Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte70PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte70ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte70Marketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 70A LITE":
        fonte70liteMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte70liteClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte70litePremium = round(i['COLUNA7'], 2) - 0.01;
        fonte70litePremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte70liteClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte70liteMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 90 BOB":
        fonte90bobMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte90bobClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte90bobPremium = round(i['COLUNA7'], 2) - 0.01;
        fonte90bobPremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte90bobClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte90bobMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 120 BOB":
        fonte120bobMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte120bobClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte120bobPremium = round(i['COLUNA7'], 2) - 0.01;
        fonte120bobPremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte120bobClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte120bobMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 120A LITE":
        fonte120liteMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte120liteClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte120litePremium = round(i['COLUNA7'], 2) - 0.01;
        fonte120litePremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte120liteClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte120liteMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 120A":
        fonte120Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte120Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte120Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte120PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte120ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte120Marketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 200 BOB":
        fonte200bobMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte200bobClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte200bobPremium = round(i['COLUNA7'], 2) - 0.01;
        fonte200bobPremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte200bobClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte200bobMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 200A LITE":
        fonte200liteMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte200liteClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte200litePremium = round(i['COLUNA7'], 2) - 0.01;
        fonte200litePremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte200liteClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte200liteMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 200 MONO":
        fonte200monoMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte200monoClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte200monoPremium = round(i['COLUNA7'], 2) - 0.01;
        fonte200monoPremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte200monoClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte200monoMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 200A":
        fonte200Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte200Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte200Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte200PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte200ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte200Marketplaceprice = round(i['SITE'], 2) - 0.01;
        
for index, i in db.iterrows():
    if i['PRODUTO'] == "FONTE 40A":
        fonte40Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte40Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte40Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte40PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte40ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte40Marketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 60A":
        fonte60Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte60Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte60Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte60PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte60ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte60Marketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 60A LITE":
        fonte60liteMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte60liteClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte60litePremium = round(i['COLUNA7'], 2) - 0.01;
        fonte60litePremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte60liteClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte60liteMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 70A":
        fonte70Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte70Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte70Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte70PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte70ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte70Marketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 70A LITE":
        fonte70liteMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte70liteClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte70litePremium = round(i['COLUNA7'], 2) - 0.01;
        fonte70litePremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte70liteClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte70liteMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 90 BOB":
        fonte90bobMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte90bobClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte90bobPremium = round(i['COLUNA7'], 2) - 0.01;
        fonte90bobPremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte90bobClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte90bobMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 120 BOB":
        fonte120bobMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte120bobClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte120bobPremium = round(i['COLUNA7'], 2) - 0.01;
        fonte120bobPremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte120bobClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte120bobMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 120A LITE":
        fonte120liteMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte120liteClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte120litePremium = round(i['COLUNA7'], 2) - 0.01;
        fonte120litePremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte120liteClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte120liteMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 120A":
        fonte120Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte120Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte120Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte120PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte120ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte120Marketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 200 BOB":
        fonte200bobMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte200bobClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte200bobPremium = round(i['COLUNA7'], 2) - 0.01;
        fonte200bobPremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte200bobClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte200bobMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 200A LITE":
        fonte200liteMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte200liteClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte200litePremium = round(i['COLUNA7'], 2) - 0.01;
        fonte200litePremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte200liteClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte200liteMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 200 MONO":
        fonte200monoMarketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte200monoClassico = round(i['COLUNA5'], 2) - 0.01;
        fonte200monoPremium = round(i['COLUNA7'], 2) - 0.01;
        fonte200monoPremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte200monoClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte200monoMarketplaceprice = round(i['SITE'], 2) - 0.01;
    elif i['PRODUTO'] == "FONTE 200A":
        fonte200Marketplace = round(i['COLUNA3'], 2) - 0.01;
        fonte200Classico = round(i['COLUNA5'], 2) - 0.01;
        fonte200Premium = round(i['COLUNA7'], 2) - 0.01;
        fonte200PremiumPrice = round(i['PREMIUM ML'], 2) - 0.01;
        fonte200ClassicoPrice = round(i['CLÁSSICO ML'], 2) - 0.01;
        fonte200Marketplaceprice = round(i['SITE'], 2) - 0.01;
        
#"search_filters": "BRAND=2466336@category=MLB3381@", #MLB2227, 22292586

def get_diferenca(price, previsto):
    return (price / previsto) * 100;
 
options_req = [
    "FONTE 40A",
    "FONTE 60A",
    "FONTE 60A LITE",
    "FONTE 70A",
    "FONTE 70A LITE",
    "FONTE 120A",
    "FONTE 120A LITE",
    "FONTE 200A",
    "FONTE 200A LITE",
    "FONTE 90 BOB",
    "FONTE 120 BOB",
    "FONTE 200 BOB",
    "FONTE 200 MONO",
]

def get_description(mlb):
    try:
        response = requests.get(f"https://api.mercadolibre.com/items/{mlb}/description")
        return response.json()['plain_text']
    except: 
        return ""
    
def get_loja(loja):
    response = requests.get(f"https://api.mercadolibre.com/sites/MLB/search?nickname={loja}")
    user_id = response.json()['results'][0]['seller']['id']
    user_response = requests.get(f"https://api.mercadolibre.com/users/{user_id}")
    address = user_response.json()['address']['city']
    state = user_response.json()['address']['state']
    return address + " - " + state
    
    
    

def get_greeting():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Bom dia!"
    elif 12 <= current_hour < 18:
        return "Boa tarde!"
    else:
        return "Boa noite!"

def enviar(grouped_by_seller):
    requests.post("http://localhost:3000/api/sendText", {
        "chatId": "120363026494101932@g.us",
        "text": f"{get_greeting()} \n Segue anúncios fora da política",
        "session": "default"
    })
    try:
        for seller, items in grouped_by_seller.items():
            dados = f"*{seller}* \n"
            time.sleep(1)
            for item in items:
                if item['listing_type'] == "gold_special":
                    item['listing_type'] = "Clássico"
                else:
                    item['listing_type'] = "Premium"
                
                loja_info = get_loja(item['seller'])
                dados =  dados + f"{item['model']} - {item['seller']} - {loja_info} - Preço Anúncio: {item['price']} - Preço Política: {item['predicted_price']} ({item['listing_type']}) \n {item['link']} \n"
            requests.post("http://localhost:3000/api/sendText", {
            "chatId": "120363026494101932@g.us",
            "text": dados,
            "session": "default"
            })
    except Exception as e:
        print(f"Erro ao enviar mensagens: {e}")    

def politica():
    urls = [
        "https://api.mercadolibre.com/sites/MLB/search?category=MLB3381&sort=price_asc&BRAND=2466336",
        "https://api.mercadolibre.com/sites/MLB/search?category=MLB3381&sort=price_asc&BRAND=22292586",
        "https://api.mercadolibre.com/sites/MLB/search?category=MLB2227&sort=price_asc&BRAND=2466336",
        "https://api.mercadolibre.com/sites/MLB/search?category=MLB2227&sort=price_asc&BRAND=22292586",
    ]

    # Lista para armazenar todos os resultados filtrados
    all_filtered_results = []

    # Loop para cada opção e para cada conjunto de parâmetros
    for option in tqdm(options_req):
        for url in urls:
            # Atualizar parâmetros com a opção atual
            params = {"q": option}

            # Inicializar offset para paginação
            offset = 0
            while True:
                # Atualizar parâmetros com o offset atual
                params['offset'] = offset

                # Fazer a requisição GET
                try:
                    response = requests.get(url, params=params)
                except Exception as e:
                    # Tentar novamente após 10 segundos em caso de erro
                    time.sleep(10)
                    response = requests.get(url, params=params)
                    print(f"Erro ao fazer a requisição para {option}: {e}")

                # Verificar se a requisição foi bem-sucedida
                if response.status_code != 200:
                    print(f"Erro ao fazer a requisição para {option} com {params}: {response.status_code}")
                    break

                data = response.json()
                results = data.get('results', [])
                total = data.get('paging', {}).get('total', 0)
                # Filtrar os resultados
                for item in results:
                    title = item.get('title', '').lower()
                    price = item.get('price', float('inf'))
                    real_price = item.get('original_price', float('inf'))
                    link = item.get('permalink', '')
                    sellernickname = item.get('sellernickname', '')
                    listing_type_id = item.get('listing_type_id', '')
                    if real_price:
                        real_price = float(real_price)
                    if option == "FONTE 40A":
                        item['modelo'] = "FONTE 40A"
                        if "bob" not in title and "lite" not in title and "light" not in title  and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "40a" in title or "40" in title or "40 amperes" in title or "40amperes" in title or "36a" in title or "36" in title or "36 amperes" in title or "36amperes" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if attribute['value_name'] is not None and ("bob" in attribute['value_name'].lower() or "lite" in attribute['value_name'].lower()):
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte40Premium:
                                    item['diferenca'] = get_diferenca(price, fonte40Premium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte40Premium
                                    item['real_price_previsto'] = fonte40PremiumPrice
                                    if real_price:
                                        if real_price < fonte40PremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte40Classico:
                                    item['diferenca'] = get_diferenca(price, fonte40Classico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte40Classico
                                    item['real_price_previsto'] = fonte40ClassicoPrice
                                    if real_price:
                                        if real_price < fonte40ClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 60A":
                        item['modelo'] = "FONTE 60A"
                        if "bob" not in title and "lite" not in title and "light" not in title  and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "60a" in title or "60" in title or "60 amperes" in title or "60amperes" in title or "60 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if "bob" in attribute['value_name'].lower() or "lite" in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte60Premium:
                                    item['diferenca'] = get_diferenca(price, fonte60Premium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte60Premium
                                    item['real_price_previsto'] = fonte60PremiumPrice
                                    if real_price:
                                        if real_price < fonte60PremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte60Classico:
                                    item['diferenca'] = get_diferenca(price, fonte60Classico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte60Classico
                                    item['real_price_previsto'] = fonte60ClassicoPrice
                                    if real_price:
                                        if real_price < fonte60ClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 60A LITE":
                        item['modelo'] = "FONTE 60A LITE"
                        if "bob" not in title and ("lite" in title or "light" in title) and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "60a" in title or "60" in title or "60 amperes" in title or "60amperes" in title or "60 a" in title: 
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if 'bob' in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte60litePremium:
                                    item['diferenca'] = get_diferenca(price, fonte60litePremium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte60litePremium
                                    item['real_price_previsto'] = fonte60litePremiumPrice
                                    if real_price:
                                        if real_price < fonte60litePremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte60liteClassico:
                                    item['diferenca'] = get_diferenca(price, fonte60liteClassico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte60liteClassico
                                    item['real_price_previsto'] = fonte60liteClassicoPrice
                                    if real_price:
                                        if real_price < fonte60liteClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                        
                    elif option == "FONTE 70A":
                        item['modelo'] = "FONTE 70A"
                        if "bob" not in title and "lite" not in title and "light" not in title  and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "70a" in title or "70" in title or "70 amperes" in title or "70amperes" in title or "70 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if "bob" in attribute['value_name'].lower() or "lite" in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte70Premium:
                                    item['diferenca'] = get_diferenca(price, fonte70Premium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte70Premium
                                    item['real_price_previsto'] = fonte70PremiumPrice
                                    if real_price:
                                        if real_price < fonte70PremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte70Classico:
                                    item['diferenca'] = get_diferenca(price, fonte70Classico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte70Classico
                                    item['real_price_previsto'] = fonte70ClassicoPrice
                                    if real_price:
                                        if real_price < fonte70ClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 70A LITE":
                        item['modelo'] = "FONTE 70A LITE"
                        if "bob" not in title and  ("lite" in title or "light" in title) and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "70a" in title or "70" in title or "70 amperes" in title or "70amperes" in title or "70 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if 'bob' in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte70litePremium:
                                    item['diferenca'] = get_diferenca(price, fonte70litePremium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte70litePremium
                                    item['real_price_previsto'] = fonte70litePremiumPrice
                                    if real_price:
                                        if real_price < fonte70litePremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte70liteClassico:
                                    item['diferenca'] = get_diferenca(price, fonte70liteClassico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte70liteClassico
                                    item['real_price_previsto'] = fonte70liteClassicoPrice
                                    if real_price:
                                        if real_price < fonte70liteClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 120A":
                        item['modelo'] = "FONTE 120A"
                        if "bob" not in title and "lite" not in title and "light" not in title  and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "120a" in title or "120" in title or "120 amperes" in title or "120amperes" in title or "120 a" in title: 
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if "bob" in attribute['value_name'].lower() or "lite" in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte120Premium:
                                    item['diferenca'] = get_diferenca(price, fonte120Premium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte120Premium
                                    item['real_price_previsto'] = fonte120PremiumPrice
                                    if real_price:
                                        if real_price < fonte120PremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte120Classico:
                                    item['diferenca'] = get_diferenca(price, fonte120Classico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte120Classico
                                    item['real_price_previsto'] = fonte120ClassicoPrice
                                    if real_price:
                                        if real_price < fonte120ClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 120A LITE":
                        item['modelo'] = "FONTE 120A LITE"
                        if "bob" not in title and  ("lite" in title or "light" in title) and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "120a" in title or "120" in title or "120 amperes" in title or "120amperes" in title or "120 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if 'bob' in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte120litePremium:
                                    item['diferenca'] = get_diferenca(price, fonte120litePremium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte120litePremium
                                    item['real_price_previsto'] = fonte120litePremiumPrice
                                    if real_price:
                                        if real_price < fonte120litePremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte120liteClassico:
                                    item['diferenca'] = get_diferenca(price, fonte120liteClassico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte120liteClassico
                                    item['real_price_previsto'] = fonte120liteClassicoPrice
                                    if real_price:
                                        if real_price < fonte120liteClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 200A":
                        item['modelo'] = "FONTE 200A"
                        if "bob" not in title and "lite" not in title and "light" not in title and "controle" not in title and 'mono' not in title and 'monovolt' not in title and "220v" not in title:
                            if "200a" in title or "200" in title or "200 amperes" in title or "200amperes" in title or "200 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if "bob" in attribute['value_name'].lower() or "lite" in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue;                                   
                                if listing_type_id == "gold_pro" and price < fonte200Premium:
                                    item['diferenca'] = get_diferenca(price, fonte200Premium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte200Premium
                                    item['real_price_previsto'] = fonte200PremiumPrice
                                    if real_price is not None:
                                        if real_price < fonte200PremiumPrice:
                                            description = get_description(item['id'])
                                            if "lite" in description.lower() or "bob" in description.lower():
                                                continue
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)
                                elif price < fonte200Classico:
                                    item['diferenca'] = get_diferenca(price, fonte200Classico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte200Classico
                                    item['real_price_previsto'] = fonte200ClassicoPrice
                                    if real_price is not None:
                                        if real_price < fonte200ClassicoPrice:
                                            all_filtered_results.append(item)
                                    else:
                                        description = get_description(item['id'])
                                        if "lite" in description.lower() or "bob" in description.lower():
                                            continue
                                        all_filtered_results.append(item)

                    elif option == "FONTE 200A LITE":
                        item['modelo'] = "FONTE 200A LITE"
                        if "bob" not in title and  ("lite" in title or "light" in title) and "controle" not in title and 'mono' not in title and 'monovolt' not in title:
                            if "200a" in title or "200" in title or "200 amperes" in title or "200amperes" in title or "200 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if 'bob' in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte200litePremium:
                                    item['diferenca'] = get_diferenca(price, fonte200litePremium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte200litePremium
                                    item['real_price_previsto'] = fonte200litePremiumPrice
                                    if real_price:
                                        if real_price < fonte200litePremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte200liteClassico:
                                    item['diferenca'] = get_diferenca(price, fonte200liteClassico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte200liteClassico
                                    item['real_price_previsto'] = fonte200liteClassicoPrice
                                    if real_price:
                                        if real_price < fonte200liteClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 90A BOB":
                        item['modelo'] = "FONTE 90A BOB"
                        if "bob" in title and "lite" not in title and "light" not in title  and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "90a" in title or "90" in title or "90 amperes" in title or "90amperes" in title or "90 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if "lite" in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte90bobPremium:
                                    item['diferenca'] = get_diferenca(price, fonte90bobPremium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte90bobPremium
                                    item['real_price_previsto'] = fonte90bobPremiumPrice
                                    if real_price:
                                        if real_price < fonte90bobPremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte90bobClassico:
                                    item['diferenca'] = get_diferenca(price, fonte90bobClassico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte90bobClassico
                                    item['real_price_previsto'] = fonte90bobClassicoPrice
                                    if real_price:
                                        if real_price < fonte90bobClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 120A BOB":
                        item['modelo'] = "FONTE 120A BOB"
                        if "bob" in title and "lite" not in title and "light" not in title  and "controle" not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "120a" in title or "120" in title or "120 amperes" in title or "120amperes" in title or "120 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if "lite" in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte120bobPremium:
                                    item['diferenca'] = get_diferenca(price, fonte120bobPremium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte120bobPremium
                                    item['real_price_previsto'] = fonte120bobPremiumPrice
                                    if real_price:
                                        if real_price < fonte120bobPremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte120bobClassico:
                                    item['diferenca'] = get_diferenca(price, fonte120bobClassico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte120bobClassico
                                    item['real_price_previsto'] = fonte120bobClassicoPrice
                                    if real_price:
                                        if real_price < fonte120bobClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 200A BOB":
                        item['modelo'] = "FONTE 200A BOB"
                        if "bob" in title and "lite" not in title and "light" not in title  and "controle" not in title and 'mono' not in title and 'mono' not in title and 'monovolt' not in title and "usina" not in title and ("jfa" in title or "fonte carregador" in title or "fonte automotiva" in title or "fonte e carregador" in title or "carregador de baterias" in title):
                            if "200a" in title or "200" in title or "200 amperes" in title or "200amperes" in title or "200 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if "lite" in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte200bobPremium:
                                    item['diferenca'] = get_diferenca(price, fonte200bobPremium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte200bobPremium
                                    item['real_price_previsto'] = fonte200bobPremiumPrice
                                    if real_price:
                                        if real_price < fonte200bobPremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte200bobClassico:
                                    item['diferenca'] = get_diferenca(price, fonte200bobClassico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte200bobClassico
                                    item['real_price_previsto'] = fonte200bobClassicoPrice
                                    if real_price:
                                        if real_price < fonte200bobClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                    elif option == "FONTE 200A MONO":
                        item['modelo'] = "FONTE 200A MONO"
                        if "bob" not in title and "lite" not in title and "light" not in title  and "controle" not in title and ("mono" in title or "220v" in title or "monovolt" in title):
                            if "200a" in title or "200" in title or "200 amperes" in title or "200amperes" in title or "200 a" in title:
                                isWrong = False
                                for attribute in item['attributes']:
                                    if attribute['value_name'] is not None:
                                        if "bob" in attribute['value_name'].lower() or "lite" in attribute['value_name'].lower():
                                            isWrong = True
                                if isWrong:
                                    continue
                                if listing_type_id == "gold_pro" and price < fonte200monoPremium:
                                    item['diferenca'] = get_diferenca(price, fonte200monoPremium)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte200monoPremium
                                    item['real_price_previsto'] = fonte200monoPremiumPrice
                                    if real_price:
                                        if real_price < fonte200monoPremiumPrice: 
                                            all_filtered_results.append(item) 
                                    else:
                                        all_filtered_results.append(item) 

                                elif price < fonte200monoClassico:
                                    item['diferenca'] = get_diferenca(price, fonte200monoClassico)
                                    if item['diferenca'] < 70:
                                        continue
                                    item['price_previsto'] = fonte200monoClassico
                                    item['real_price_previsto'] = fonte200monoClassicoPrice
                                    if real_price:
                                        if real_price < fonte200monoClassicoPrice: 
                                            all_filtered_results.append(item)
                                    else:
                                        all_filtered_results.append(item)

                        

                # Atualizar o offset para a próxima página
                offset += 50

                # Verificar se todos os itens foram processados
                if offset >= total:
                    break
                
    formatted_results = [
        {
            "image": result['thumbnail'],
            "model": result['modelo'],
            "seller": result['seller']['nickname'],
            "title": result['title'],
            "price": result['price'],   
            "predicted_price": result['price_previsto'],
            "listing_type": result['listing_type_id'],
            "link": result['permalink'],
        }
        for result in all_filtered_results
    ]
    grouped_by_seller = defaultdict(list)

    for item in formatted_results:
        seller = item['seller']
        grouped_by_seller[seller].append(item)
        
    grouped_by_seller = dict(grouped_by_seller)
        
    enviar(grouped_by_seller)



def executar_codigo():
    politica()

# Agendar a execução nos horários especificados
schedule.every().day.at("07:50").do(executar_codigo)
schedule.every().day.at("10:50").do(executar_codigo)
schedule.every().day.at("13:50").do(executar_codigo)
schedule.every().day.at("15:50").do(executar_codigo)
schedule.every().day.at("19:50").do(executar_codigo)
schedule.every().day.at("23:50").do(executar_codigo)

while True:
    schedule.run_pending()
    time.sleep(60) 