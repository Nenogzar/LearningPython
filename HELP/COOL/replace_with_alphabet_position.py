import string
def alphabet_position(text):
     return ' '.join(list(map(lambda n:str(([*(string.ascii_lowercase)]).index(n)+1),
                              filter(lambda x:str.isalpha(x),[*((text.lower()))]))))

print(alphabet_position(input("input text: ")))