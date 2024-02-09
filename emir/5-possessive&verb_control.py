with open("finals.txt", "r", encoding="utf-8") as file:
    words = file.readlines()

cleaned_words = []
for word in words:
    word = word.strip() 
    if not word.endswith(( "lik", "lık", "luk", "lük",
    "ci", "cı", "cu", "cü",
    "ken",
    "ce",
    "er", "ar", "ır", "ir", "ur", "ür",
    "mek", "mak",
    "iş", "ış", "üş", "ış",
    "dir", "tir",
    "li", "lı", "lu", "lü",
    "siz", "sız", "suz", "süz",
    "msi", "imsi",
    "ncı", "ncu", "nçi", "nçu",
    "ce", "ca", "ça",
    "ken",
    "de", "da", "te", "ta",
    "me", "ma",
    "di", "ti", "dı", "tı",
    "de", "da", "te", "ta",
    "den", "dan", "ten", "tan","erek","arak", "im","ım","üm,","in","ın","un","ün","i","ı","u","ü",
    "imiz","ımız","umuz","ümüz","iniz","ınız","unuz","ünüz","an","en","le","la","dum","dim","din","dün","dan","den","de","da",
    "ya","ye","yü","yu","ip","ıp","up","üp","ler","lar","lere","lara","leri","ecek","acak","yor","ine","ına","una","üne","mize","mıza","nıza","nize",
    "mez","maz","müz","muz","rum","rim","rüm","rım","mem","mam","um","sa","se","meniz","manız","mımız","ma","mamız","me","na","ne")):
        cleaned_words.append(word)

with open("finals.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(cleaned_words))

print("Deleted.")
