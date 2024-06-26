north_america_premise = 1/12
europeans_premise = 1/4
africa_premise = 1/9
asia_premise = 1/6
other_continents_premise = 42

north_america_hypothesis = 1/12
europeans_hypothesis = 1/4
africa_hypothesis = 1/9
asia_hypothesis = 1/6
other_continents_hypothesis = 42

# the hypothesis refers to the same proportions of passengers on a ship mentioned in the premise
if north_america_hypothesis >= north_america_premise:
    # check if the hypothesis value contradicts the estimate of less than 'north_america_premise'
    label = "contradiction"
elif europeans_hypothesis!= europeans_premise:
    # check if the number of Europeans in the hypothesis contradicts the number of Europeans reported in the premise
    label = "contradiction"
elif africa_hypothesis!= africa_premise:
    # check if the number of Africans in the hypothesis contradicts the number of Africans reported in the premise
    label = "contradiction"
elif asia_hypothesis!= asia_premise:
    # check if the number of Asians in the hypothesis contradicts the number of Asians reported in the premise
    label = "contradiction"
elif other_continents_hypothesis!= other_continents_premise:
    # check if the number of other continents in the hypothesis contradicts the number of other continents reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
