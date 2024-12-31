import requests
import datetime

bugun =f'{datetime.datetime.today().date().day}-{datetime.datetime.today().date().month}-{datetime.datetime.today().date().year}'

def prayerTime(manzil):
    url = f"https://api.aladhan.com/v1/timingsByAddress/{bugun}?address={manzil}&method=1"
    try:
        respons = requests.get(url)

        fajr = respons.json()['data']["timings"]["Fajr"]
        sun_rise = respons.json()['data']["timings"]["Sunrise"]
        dhuhr = respons.json()['data']["timings"]["Dhuhr"]
        asr = respons.json()['data']["timings"]["Asr"]
        maghrib = respons.json()['data']["timings"]["Maghrib"]
        isha = respons.json()['data']["timings"]["Isha"]

        prayer_times = {"fajr":fajr,"sun_rise":sun_rise,"dhuhr":dhuhr,"asr":asr,"maghrib":maghrib,"isha":isha}

        return prayer_times
    except:
        return f"Unday manzil topilmadi"

