import requests

def getCryptoData():
    response= requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code==200:
        return response.json()

cryptoResponse= getCryptoData()
userinput= input("Enter your crypto currency: ")
for crypto in cryptoResponse:
    if crypto["currency"]==userinput:
        print(crypto["price"])
        break