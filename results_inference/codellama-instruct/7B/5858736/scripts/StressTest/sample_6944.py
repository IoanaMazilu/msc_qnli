jill_city_premise = "City C"
cities_visited_premise = 7
cities_visited_hypothesis = 6

# the hypothesis talks about the number of cities visited, referenced also in the premise
if cities_visited_hypothesis <= cities_visited_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cities_visited_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cities visited
    # any number of cities greater than 'cities_visited_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
