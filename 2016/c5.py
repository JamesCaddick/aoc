import hashlib

data = 'cxdnnyjw'

c = 0
i = 0
password = {}
while c < 8:
    hexidecimal = hashlib.md5((data + str(i)).encode('utf-8')).hexdigest()
    i += 1
    try:
        idx = int(hexidecimal[5])
    except ValueError:
        idx = 99
    if hexidecimal.startswith('00000') and idx < 8 and idx != 99 and idx not in password:
        password[idx] = hexidecimal[6]
        c += 1
password = password[0] + password[1] + password[2] + password[3] + password[4] + password[5] + password[6] + password[7]
print(password)