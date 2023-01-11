import re

with open('i7.txt') as f:
    data = f.readlines()
data = [d.strip() for d in data]
# answer = 0
# for d in data:
#     hypertext_pattern = r'\[[a-z]+\]'
#     ip_pattern = r'[a-z]+'
#     abba_pattern = r'(.)(.)\2\1'
#     hypertext = re.findall(hypertext_pattern, d)
#     ip = re.findall(ip_pattern, d)
#     hypertext_status = False
#     ip_status = False
#     for h in hypertext:
#         hypertext_matches = re.findall(abba_pattern, h)
#         for hm in hypertext_matches:
#             if hm[0] != hm[1]:
#                 hypertext_status = True
#     for i in ip:
#         ip_matches = re.findall(abba_pattern, i)
#         for ipm in ip_matches:
#             if ipm[0] != ipm[1]:
#                 ip_status = True
#     if not hypertext_status and ip_status:
#         answer += 1
# print(answer)

answer2 = 0
for d in data:
    match_status = False
    matches = re.findall(r'(.)(.)\1.*\[[a-z]*\2\1\2[a-z]*\]|\[[a-z]*(.)(.)\3[a-z]*\].*\4\3\4', d)
    for m in matches:
        if m:
            if m[0] != m[1] or m[2] != m[3]:
                match_status = True
    if match_status:
        answer2 += 1
print(answer2)