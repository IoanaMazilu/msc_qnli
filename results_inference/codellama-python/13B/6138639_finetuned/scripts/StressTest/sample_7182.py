north_america_premise = 1/12
north_america_hypothesis = 4/12
europeans_premise = 1/8
europeans_hypothesis = 1/8
africa_premise = 1/3
africa_hypothesis = 1/3
asia_premise = 1/6
asia_hypothesis = 1/6
other_continents_premise = 35
other_continents_hypothesis = 35

# the hypothesis refers to the same proportions of passengers on a ship mentioned in the premise
if north_america_hypothesis >= north_america_premise:
    # check if the estimate of 'north_america_hypothesis' contradicts the proportion of passengers in the premise
    label = "contradiction"
elif europeans_hypothesis!= europeans_premise:
    # check if the proportion of passengers in the hypothesis contradicts the proportion of passengers in the premise
    label = "contradiction"
elif africa_hypothesis!= africa_premise:
    # check if the proportion of passengers in the hypothesis contradicts the proportion of passengers in the premise
    label = "contradiction"
elif asia_hypothesis!= asia_premise:
    # check if the proportion of passengers in the hypothesis contradicts the proportion of passengers in the premise
    label = "contradiction"
elif other_continents_hypothesis!= other_continents_premise:
    # check if the proportion of passengers in the hypothesis contradicts the proportion of passengers in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
