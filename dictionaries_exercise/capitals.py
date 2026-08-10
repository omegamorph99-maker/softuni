country = input().split(', ')
capital = input().split(', ')
dictionary_of_countries = {zip(country, capital)}

for key in dictionary_of_countries.keys():
    print(f'{key} -> {value}')