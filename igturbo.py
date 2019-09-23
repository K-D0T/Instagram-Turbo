import time 
from urllib.request import urlopen as uReq
import requests 
import json
import getpass
import ctypes

print("                                                                           ")
print("                             |K-DOT'S IGTURBO|                             ")
print("___________________________________________________________________________")

EMAIL = '' # input("Your email: ") 
PASS = '' #getpass.getpass("Password: ")
PHONE = '' #input("Your phone number Ex +1 123-456-7890: ")
USER = input("Wanted username: ")
   
username = True

with requests.Session() as c:
    url = 'https://www.instagram.com/accounts/login/ajax/'

    headers = {
        'content-type':'application/x-www-form-urlencoded',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept':'*/*',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/accounts/login/?source=auth_switcher',
        'x-requested-with':'XMLHttpRequest',
        'x-instagram-ajax':'0c2539981709',
        'x-ig-app-id':'936619743392459'
    }
        #grabbing the csrf token from the cookies we received from the get request.
    csrf_grab = c.get(url, headers=headers)
    CSRF1 = csrf_grab.cookies['csrftoken']
        #Adding CSRF token to header
    headers = {
        'content-type':'application/x-www-form-urlencoded',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept':'*/*',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/accounts/login/?source=auth_switcher',
        'x-requested-with':'XMLHttpRequest',
        'x-instagram-ajax':'0c2539981709',
        'x-ig-app-id':'936619743392459',
        'x-csrftoken': CSRF1
    }
        #Creating the post payload
    payload = {'username': EMAIL,'password': PASS}
        #Sending the login request
    login = c.post(url, headers=headers, data=payload)
    print(login.text)

        #Checking to see if we successfully logged in
    if '{"authenticated": true' in login.text:
        print("Login Successful, starting turbo...")
        url = 'https://www.instagram.com/accounts/edit'

    else:
        print("Login unsuccessful")
while username == True:
    try:
        
        r = requests.get('https://www.instagram.com/' + USER)
            
 

        if r.status_code == 200:
            username = True 
            #print("Trying", target)
            #time.sleep(.2)
        elif r.status_code == 429:

            username = True

        else:        
            print(USER,"Now Available")
            username = False
            start = time.time()

            break  

    except:
        print("Connection error")
        time.sleep(1)
        continue 

if username == False:
    start = time.time()
   


    

    headers = {
        'content-type':'application/x-www-form-urlencoded',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept':'*/*',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/accounts/edit/',
        'x-requested-with':'XMLHttpRequest',
        'x-instagram-ajax':'6cb19191eaa3',
        'x-ig-app-id':'936619743392459'
    }

    csrf_grab = c.get(url, headers=headers)
    CSRF2 = csrf_grab.cookies['csrftoken']

    headers = {
        'content-type':'application/x-www-form-urlencoded',
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept':'*/*',
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/accounts/edit/',
        'x-requested-with':'XMLHttpRequest',
        'x-instagram-ajax':'6cb19191eaa3',
        'x-ig-app-id':'936619743392459',
        'x-csrftoken': CSRF2
    }
            #Instagram makes the edit post request contain all information at once so if you need to also create a varaible for name
    payload = {'first_name':'','email':EMAIL,'username':USER,'phone_number':PHONE,'gender':1, 'biography':'', 'external_url':'','chaining_enabled':'on'}

    edit = c.post(url, headers=headers, data=payload)

    #This is the success key for a Username being changed
    if '{"status": "ok"}':
        end = time.time()
        print('Successfully Changed Username in', end - start, '')
        ctypes.windll.user32.MessageBoxW(0, USER , "|K-DOT'S IGTURBO| YOU COPPED: ", 1)

    else:
        'An error occured while trying to change Usernames'

else:
    print('An error has occured either the server rejected your request or you entered invalid credentials')






