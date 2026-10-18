# poppybanya_string_counter.py

poppybanya_items = [
    "poppy_seeds", 42, "steam_towel", 3.14, True, "herbal_tea", None, "sauna_hat", 7,
]

string_count = 0
for item in poppybanya_items:
    if isinstance(item, str):
        string_count += 1

print("Total items:", len(poppybanya_items))
print("String items:", string_count)
