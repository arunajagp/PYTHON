mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(mydict)
print(mydict.copy())
x=0
print(dict.fromkeys(mydict,x))
print(mydict.get("year"))
print(mydict.items())
print(mydict.pop("brand"))
print(mydict.values())
print(mydict.setdefault("model", "Bronco"))
print(mydict.clear())
