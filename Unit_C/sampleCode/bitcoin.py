import json

fileName = "bitcoin.json"
f = open(fileName)
b = json.load(f)
f.close()
print(b)
chartName = b["chartName"]
bpi = b["bpi"]
usDollars = bpi["USD"]
rate = usDollars["rate_float"]

time = b["time"]["updateduk"]
rateTheHardWay = b["bpi"]["USD"]["rate_float"]

print(f"\nThe chart Name is {chartName}")
print(f"\nThe bpi is {bpi}")
print(f"\nThe US Dollars dictionary is {usDollars}")
print(f"\nFINALLY, we get the rate.  The price of bitcoin is {rate}")
print(f"The above is current as of {time}")
print(f"Rate caluculate the long ways is {rateTheHardWay}")