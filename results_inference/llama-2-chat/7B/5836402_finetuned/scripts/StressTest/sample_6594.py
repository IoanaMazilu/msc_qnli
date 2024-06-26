cities_premise = 9
cities_hypothesis = 1

# the hypothesis talks about the number of cities in a province in France, referenced also in the premise
if cities_hypothesis <= cities_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cities_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cities
    # any number of cities greater than 'cities_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
