import requests as rs

lat=input('Enter the latitude : ')
lng=input('Enter the longitude : ')

curl=f'https://api.sunrisesunset.io/json?lat={lat}&lng={lng}'

cheader={
'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
}
c_Resp=rs.get(url=curl,headers=cheader)

decode=(c_Resp.json())


if c_Resp.status_code == 200:
    print(f'URL Valid = {c_Resp.status_code}')
    print(decode)
else:
    print('You enter the Invalid lat and lng my Frnd !')






