word='sos'
output=[]
alphabet2morse={
    's':[0,0,0],
    'o':[1,1,1]
}
for letter in word:
    output=output+alphabet2morse[letter]
print(output)

