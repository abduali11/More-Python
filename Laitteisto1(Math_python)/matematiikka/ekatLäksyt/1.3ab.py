import math
#taulukko
asteet = [30, 40, 50, 60,90,120,135,150,180,270,360]
radiaanit = [math.radians(asteet) for asteet in asteet]
print(f"Radiaanit asteina on : {radiaanit}")

