# Premise: In a certain province in France there are less than 25 cities.
# Hypothesis: In a certain province in France there are 15 cities.
# Golden Label: neutral

cities_province_premise = 25
cities_province_hypothesis = 15

# the hypothesis refers to the number of cities in a province, also mentioned in the premise
if cities_province_hypothesis >= cities_province_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cities_province_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cities
    # any number of cities less than 'cities_province_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

