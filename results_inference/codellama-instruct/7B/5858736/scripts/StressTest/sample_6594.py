cities_province_premise = 9
cities_province_hypothesis = 1

if cities_province_hypothesis <= cities_province_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
