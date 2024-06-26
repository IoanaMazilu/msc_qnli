cities_premise = 81
cities_hypothesis = 11

# the hypothesis talks about the number of cities in a certain province in France, also referenced in the premise
if cities_hypothesis >= cities_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cities_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cities
    # any number of cities less than 'cities_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
