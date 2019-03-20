f = open("sonnet.txt", "r")

text = f.read()

f.close()

i = 0
for letter in text:
    if letter.lower() in 'aeiou':
        i +=1
print(i)



a = open("all star lyrics.txt", "r")

text = a.read()

a.close()
e = 0
for letter in text:
    if letter.lower() in 'aeiou':
        e +=1
print(e)

q = 0
for letter in text:
    if letter == ' ' or letter == '\n':
        q +=1
print(q)

r=0
u = 0
re = 0
ue = 0

for letter in text:
    if letter == '\n':


        if r > re:
            ue = u
            re = r
        r =0
        u += 1
    else:
        r +=1
print(ue)
