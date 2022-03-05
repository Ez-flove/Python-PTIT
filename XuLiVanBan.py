text = ""
while True: 
    try: 
        text += input().lower()+" "
    except EOFError: 
        break
text=text.replace('?',".").replace('!',".").strip()
s=text.split(".")
for i in s:
    ss=i.strip().capitalize().split()
    for j in ss:
        print(j,end=" ")
    print()