import threading
from time import sleep
from bs4 import BeautifulSoup
import requests
import csv

def deepScraping(card):
  link = card.find_next("a")
  link = requests.get('https://mundimoto.com'+link.get('href'))
  soup2 = BeautifulSoup(link.text,"html.parser")
  capacity = None
  capacity_pre = soup2.find_all("span", class_="information-text")
  capacity_text = ""
  if(len(capacity_pre)>2 and "c.c." in capacity_pre[2].string ):
    for y in capacity_pre[2]:
        for z in y.string:
            if z.isnumeric():
                capacity_text += z
  if(capacity_text != ""):
    capacity = int(capacity_text)
  price_pre = card.find_next("span", class_="price") or card.find_next(
      "span", class_="promo_original"
  )
  brands = card.find_all("h2", class_="brand")
  brand = brands[0].string.strip()
  model = brands[1].string.replace("promo","").strip()
  moto_details = card.find_all("span", class_="moto-details")
  mtype = moto_details[0].string.strip()
  year = int(moto_details[1].string.strip())
  distance_pre = moto_details[2]
  license = moto_details[3].string.strip()

  price_txt = ""
  for y in price_pre:
      for z in y.string:
          if z.isnumeric():
              price_txt += z
  distance_txt = ""
  for y in distance_pre:
      for z in y.string:
          if z.isnumeric():
              distance_txt += z

  if price_txt != "":
      price = int(price_txt)
      distance = int(distance_txt)
      print({
              "Brand": brand,
              "Model": model,
              "Kms": distance,
              "License": license,
              "Year": year,
              "Capacity": capacity,
              "Type": mtype,
              "Price": price,
          })
      writer.writerow(
          {
              "Brand": brand,
              "Model": model,
              "Kms": distance,
              "License": license,
              "Year": year,
              "Capacity": capacity,
              "Type": mtype,
              "Price": price,
          }
      )
with open("motoDatasetFinal.csv", mode="w") as csv_file:
    fieldnames = [
        "Brand",
        "Model",
        "Kms",
        "License",
        "Year",
        "Capacity",
        "Type",
        "Price",
    ]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    with open("out.html", "r") as f:
        soup = BeautifulSoup(f, "html.parser")
        cards = soup.find_all("app-product-card")
        limit = len(cards)
        offset = 0
        while(offset<limit):
            t1 = threading.Thread(target=deepScraping, args=(cards[offset]))
            t1.start()
            if(offset+1<limit):
              t2 = threading.Thread(target=deepScraping, args=(cards[offset+1]))
              t2.start()
            if(offset+2<limit):
              t3 = threading.Thread(target=deepScraping, args=(cards[offset+2]))
              t3.start()
            if(offset+3<limit):
              t4 = threading.Thread(target=deepScraping, args=(cards[offset+3]))
              t4.start()
            if(offset+4<limit):
              t5 = threading.Thread(target=deepScraping, args=(cards[offset+4]))
              t5.start()
            if(offset+5<limit):
              t6 = threading.Thread(target=deepScraping, args=(cards[offset+5]))
              t6.start()
            if(offset+6<limit):
              t7 = threading.Thread(target=deepScraping, args=(cards[offset+6]))
              t7.start()
            if(offset+7<limit):
              t8 = threading.Thread(target=deepScraping, args=(cards[offset+7]))
              t8.start()
            t1.join()
            if(offset+1<limit):
              t2.join()
            if(offset+2<limit):
              t3.join()
            if(offset+3<limit):
              t4.join()
            if(offset+4<limit):
              t5.join()
            if(offset+5<limit):
              t6.join()
            if(offset+6<limit):
              t7.join()
            if(offset+7<limit):
              t8.join()
            offset+=8
        print("DOne")

