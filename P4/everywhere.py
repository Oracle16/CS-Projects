# ===================================================================================
# file: everywhere.py
# author: Oracle16
# date: 03/03/2025
# ===================================================================================


T = int(input(""))   # number of tests
cities = []
uniqueCities = 0

for T in range(0, T):
    n = int(input(""))   # number of work trips Alice has taken so far (max 100)

    for n in range(0, n):
        cityName = input("")
        if cityName in cities:
            continue
        else:
            cities.append(cityName)

    print(len(cities))
    cities = []