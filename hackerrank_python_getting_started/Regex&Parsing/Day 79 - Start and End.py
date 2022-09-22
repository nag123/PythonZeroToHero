import re
''' m = re.search(r'\d+','1234')
    print((m.start(),m.end()))
    print(m.start())
'''
if __name__ =="__main__":
    s,k=input(),input()
    m=list(re.finditer('(?=(%s))'%k,s))
    if not m:
        print((-1,-1))
    for i in m:
        print((i.start(1),i.end(1)-1))