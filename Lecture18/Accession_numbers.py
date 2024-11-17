import re
accession=["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

#contain the number5
print("contain the number5:")
for acc in accession:
    result=re.search(r'5',acc)
    if result:
        print(acc)
print("\t")
  
#contain the letter d or e
print("contain the letter d or e:")
for acc in accession:
    result=re.search(r'[de]',acc)
    if result:
        print(acc)
print("\t")
  
#contain the letters d and e in that order
print("contain the letters d and e in that order:")
for acc in accession:
    result=re.search(r'de',acc)
    if result:
        print(acc)
print("\t")

#contain the letters d and e in that order with a single letter between them
print("contain the letters d and e in that order with a single letter between them:")
for acc in accession:
    result=re.search(r'd.e',acc)
    if result:
        print(acc)
print("\t")

#contain both the letters d and e in any order
print("contain both the letters d and e in any order:")
for acc in accession:
    resultd=re.search(r'd',acc)
    resulte=re.search(r'e',acc)
    if resultd and resulte:
        print(acc)
print("\t")

#start with x or y
print("start with x or y:")
for acc in accession:
    resultx=re.search(r'^x',acc)
    resulty=re.search(r'^y',acc)
    if resultx or resulty:
        print(acc)
print("\t")

#start with x or y and end with e
print("start with x or y and end with e:")
for acc in accession:
    resultx=re.search(r'^x',acc)
    resulty=re.search(r'^y',acc)
    resulte=re.search(r'e$',acc)
    if (resultx or resulty) and resulte:
        print(acc)
print("\t")

#contains 3 different numbers in the accession
print("contains 3 different numbers in the accession:")
for acc in accession:
    result=re.findall(r'\d',acc)
    if len(result)==3:
        print(acc)
print("\t")

#contain three or more numbers in a row
print("contains 3 different numbers in the accession:")
for acc in accession:
    result=re.findall(r'\d',acc)
    if len(result)>=3:
        print(acc)
print("\t")

#end with d followed by either a, r or p
for acc in accession:
    result = re.search(r'd[arp]$', acc)
    if result:
        print(acc)


#´ð°¸
#start with x or y
if acc.startwith('x') or acc.startswith('y'):
if re.search(r'[xy]',acc):
#start with x or y and end with e
if (acc.startswith('x') or acc.startswith('y')) and acc.endwith('e'):
if re.search('(^x|^y).+e$',acc):
if re.search('[xy].+e$',acc):
#contain three or more numbers in a row
if len(set(re.findall(r'\d',acc))) ==3 :
if re.search(r'[0123456789]{3,}',acc):

