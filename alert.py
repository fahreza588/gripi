import requests,time,link,tele
import json

while True:
    for strig in link.urls:
        try:
            domain = strig.split("//")[1].split("/")[0].replace(".co.id", '').replace(".app", '').replace(".", '_').replace(
                ".com", '').replace(".id", '').replace("-", "_")

            code = strig.split("/c/")[1]
            try:
                code = code.split("?")[0]
            except:
                pass
            code = code.replace("?", "")
            #print("-----------------------------------------------------------------------------------------")
            #print("                           ******** SCRIP GRIVY NOTIF ******** ")
            #print("-----------------------------------------------------------------------------------------")
            print(domain, code)

            payload = json.dumps({"data": {"publicCode": code, "domain": domain}})
            headers = {
                'authority': 'us-central1-grivy-barcode.cloudfunctions.net',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9,ru;q=0.8,id;q=0.7',
                'content-type': 'application/json',
                'dnt': '1',
                'origin': 'https://grivy.app',
                'referer': 'https://grivy.app/',
                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
            }

            url_main = "https://us-central1-grivy-barcode.cloudfunctions.net/getCampaign"

            response = requests.post(url_main, headers=headers, data=payload).json()

            if "result" in response and "campaign_status" in response["result"]:
                if "active" in response['result']['campaign_status']:
                    if "False" in str(response['result']['coupons_finished']):
                        if "False" in str(response['result']['expired']):
                            msg = f"[{time.strftime('%X')}] {strig} [Voucher Ready]"
                            to_url = f"https://api.telegram.org/bot{tele.token1}/sendMessage?chat_id={tele.group_id1}&text={msg}"
                            #to_url2 = f"https://api.telegram.org/bot{tele.token2}/sendMessage?chat_id={tele.group_id2}&text={msg}"
                            #to_url3 = f"https://api.telegram.org/bot{tele.token3}/sendMessage?chat_id={tele.group_id3}&text={msg}"
                            #to_url4 = f"https://api.telegram.org/bot{tele.token4}/sendMessage?chat_id={tele.group_id4}&text={msg}"
                            #to_url5 = f"https://api.telegram.org/bot{tele.token5}/sendMessage?chat_id={tele.group_id5}&text={msg}"
                            #to_url6 = f"https://api.telegram.org/bot{tele.token6}/sendMessage?chat_id={tele.group_id6}&text={msg}"
                            #to_url7 = f"https://api.telegram.org/bot{tele.token7}/sendMessage?chat_id={tele.group_id7}&text={msg}"
                            #to_url8 = f"https://api.telegram.org/bot{tele.token8}/sendMessage?chat_id={tele.group_id8}&text={msg}"
                            #to_url9 = f"https://api.telegram.org/bot{tele.token9}/sendMessage?chat_id={tele.group_id9}&text={msg}"
                            #to_url10 = f"https://api.telegram.org/bot{tele.token10}/sendMessage?chat_id={tele.group_id10}&text={msg}"

                            # Kirim pesan ke semua URL Telegram yang diatur
                            for url_telegram in [to_url]:
                                resp = requests.get(url_telegram)
                                get_data = resp.text
                                if "true" in get_data:
                                    print(f"[{time.strftime('%X')}] [ Voucher Ready ]")
                                elif "false" in get_data:
                                    print(f"[{time.strftime('%X')}] [ Voucher Ready ]")
                        else:
                            print(f"[{time.strftime('%X')}] {strig} [ Belum ready ]")
                    else:
                        print(f"[{time.strftime('%X')}] {strig} [ Belum ready ]")
                else:
                    print(f"[{time.strftime('%X')}] {strig} [ Belum ready ]")
            else:
                print(f"[{time.strftime('%X')}] {strig} [ Gagal mendapatkan data dari API Grivy ]")
                
        except Exception as e:
            pass

    # Jeda selama 5 menit sebelum iterasi berikutnya
    time.sleep(10)  # 300 detik = 5 menit
