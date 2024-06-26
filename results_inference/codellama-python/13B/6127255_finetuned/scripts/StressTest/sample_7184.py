north_america_passengers_premise = 1/12
north_america_passengers_hypothesis = 3/12
europe_passengers = 1/8
africa_passengers = 1/3
asia_passengers = 1/6
other_passengers = 35

# the hypothesis refers to the same distribution of passengers on a ship as in the premise
if north_america_passengers_hypothesis!= north_america_passengers_premise:
    # check if the fraction of North American passengers in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
