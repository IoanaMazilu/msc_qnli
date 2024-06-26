cities_premise = 8
cities_hypothesis = 7

# the hypothesis talks about the number of cities Jill plans to visit, referenced also in the premise
if cities_hypothesis >= cities_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cities_premise'
    label = "contradiction"
elif cities_hypothesis < cities_premise:
    # the premise gives an estimate for the number of cities
    # the exact number of cities in the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)
