north_america_passengers_premise = 1/12
european_passengers_premise = 1/4
african_passengers_premise = 1/9
asian_passengers_premise = 1/6
other_continents_passengers_premise = 42

north_america_passengers_hypothesis = 1/12
european_passengers_hypothesis = 1/4
african_passengers_hypothesis = 1/9
asian_passengers_hypothesis = 1/6
other_continents_passengers_hypothesis = 42

# the hypothesis refers to the number of passengers on the ship, referenced also in the premise
if north_america_passengers_hypothesis >= north_america_passengers_premise:
    # check if the estimate of 'north_america_passengers_hypothesis' contradicts the number of passengers from North America in the premise
    label = "contradiction"
elif european_passengers_hypothesis >= european_passengers_premise:
    # check if the estimate of 'european_passengers_hypothesis' contradicts the number of passengers from Europe in the premise
    label = "contradiction"
elif african_passengers_hypothesis >= african_passengers_premise:
    # check if the estimate of 'african_passengers_hypothesis' contradicts the number of passengers from Africa in the premise
    label = "contradiction"
elif asian_passengers_hypothesis >= asian_passengers_premise:
    # check if the estimate of 'asian_passengers_hypothesis' contradicts the number of passengers from Asia in the premise
    label = "contradiction"
elif other_continents_passengers_hypothesis >= other_continents_passengers_premise:
    # check if the estimate of 'other_continents_passengers_hypothesis' contradicts the number of passengers from other continents in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
