# sub 0 - inghetat
# 0-15 - frig
# 15-30 - placut
# 30+ - canicula
temp = float(input())
if temp == 0:
    print(f"{temp}", "inghet")
elif 0 <= temp < 15:
    print(f"{temp}", "frig")
elif 15 <= temp < 30:
    print(f"{temp}", "placut")
else:
    print(f"{temp}", "canicula")
