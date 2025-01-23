import xmltodict

with open("moedas.xml","rb") as arquivo_moedas:
    dic_moedas = xmltodict.parse(arquivo_moedas)

print(dic_moedas)