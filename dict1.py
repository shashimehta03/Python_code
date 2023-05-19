my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}
keys = list(my_dict.keys())
values = list(my_dict.values())
sorted_values = sorted(values, reverse=True)
top_3_values = sorted_values[:3]
top_3_keys = []
for key, value in my_dict.items():
    if value in top_3_values:
        top_3_keys.append(key)
print("Top 3 keys:", top_3_keys)
print("Top 3 values:", top_3_values)