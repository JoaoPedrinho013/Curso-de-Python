# Crie um código em Python que teste se o
# site pudim está acessível pelo computador usado.
import requests
import urllib
import urllib.request
site = 'http://pudim.com.br'
try:
    requests.get(site)

except Exception as e:
    print('\033[91mO site pudim não esta acessivel no momento! =((\033[m')
else:

    print('\033[92mConsegui acessar o site Pudim com sucesso =))\033[m')

try:
    urllib.request.urlopen(site)
except urllib.error.URLError:  # erro usado nessa biblioteca

    print('\033[91mO site pudim não esta acessivel no momento! =(\033[m')
else:
    print('\033[92mConsegui acessar o site Pudim com sucesso =D\033[m')


