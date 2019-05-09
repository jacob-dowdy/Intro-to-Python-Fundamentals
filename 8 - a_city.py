# [ ] Iterate through the "cities" list using "for"/"in"
# [ ] sort into lists with "A" in the city name and without "A" in the name: a_city & no_a_city

cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
a_city = ""
no_a_city = ""

for city in cities:
    if "a" in city.lower():
        a_city += city + "\n"
    else:
        no_a_city += city + "\n"

print(a_city)
print(no_a_city)
