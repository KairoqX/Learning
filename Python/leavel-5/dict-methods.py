marks = {
    "Marin": 70,
    "Mahiru": 99,
    "Waguri": 98,
    0: "KairoqX"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Mahiru": 100})
marks.update({"Alya": 99})
print(marks.get("Mahiru"))
print(marks["Mahiru"])
