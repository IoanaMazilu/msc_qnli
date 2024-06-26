north_america_premise = 1/12
north_america_hypothesis = 1/12
europe_premise = 1/4
europe_hypothesis = 1/4
africa_premise = 2/9
africa_hypothesis = 2/9
asia_premise = 1/6
asia_hypothesis = 1/6
other_continents_premise = 50
other_continents_hypothesis = 50

# the hypothesis refers to the proportion of passengers from different continents, also referenced in the premise
if north_america_hypothesis!= north_america_premise or europe_hypothesis!= europe_premise or africa_hypothesis!= africa_premise or asia_hypothesis!= asia_premise or other_continents_hypothesis!= other_continents_premise:
    # check if the proportions of passengers in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passengers
    # any number of passengers consistent with the proportions in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
