laptop={"make":"hp","color":"balck","weigt":"1.4",
        "year":"2030"}

print(laptop["make"])
print(laptop["color"])
laptop["size"]="1200mm x 6000mm"

for key,value in laptop.items():
    print(key)
    print("\n")
    print(value)
