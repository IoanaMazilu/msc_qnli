north_america_passengers_premise = 4/12
north_america_passengers_hypothesis = 1/12
europe_passengers_premise = 1/8
europe_passengers_hypothesis = 1/8
africa_passengers_premise = 1/3
africa_passengers_hypothesis = 1/3
asia_passengers_premise = 1/6
asia_passengers_hypothesis = 1/6
other_continents_passengers_premise = 35
other_continents_passengers_hypothesis = 35

# the hypothesis refers to the same distribution of passengers on a ship as the premise
# but changes the fraction of passengers from North America
if north_america_passengers_hypothesis >= north_america_passengers_premise:
    # check if the fraction of North American passengers in the hypothesis contradicts the premise
    label = "contradiction"
elif europe_passengers_hypothesis!= europe_passengers_premise or \
    africa_passengers_hypothesis!= africa_passengers_premise or \
    asia_passengers_hypothesis!= asia_passengers_premise or \
    other_continents_passengers_hypothesis!= other_continents_passengers_premise:
    # check if the number of passengers from other continents in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
