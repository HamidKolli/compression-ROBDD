from mailbox import MaildirMessage


def decomposition(number):
    l = []
    while number != 0 :
        l.append(number % 2 == 1)
        number = number // 2
    return l




def completion(l,length):
    if len(l) >= length:
        return l[:length]
    i = 0
    while i+len(l) <= length :
        l.append(False)
        i+=1
    return l


def table(x,n):
    return completion(decomposition(x),n)

class TreeException  (Exception):
    def __init__(self, s):
        super().__init__(s)




