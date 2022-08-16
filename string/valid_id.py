# s= "avinash"
# s.count("a")
# # print(s.count('a')

def isvalidIp(ip):
    count = 0
    for ch in ip:
        if not (ch == "." or (ch >= '0' and ch <= '9')):
            return False
        if ch == '.':
            count = count + 1
    if count != 3:
        return False
    parts = ip.split('.')
    print(parts)
    if len(parts) != 4:
        return False
    for x in parts:
        if x == ' ':
            return False
        n = int(x)
        if n<0 or n>255:
            return False
    return True

print(isvalidIp("125.156.254.300"))
