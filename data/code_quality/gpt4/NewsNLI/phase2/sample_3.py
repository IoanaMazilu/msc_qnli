fatalities_premise = 79
fatalities_hypothesis = 79
injured_premise = 170
injured_hypothesis = 170

# the hypothesis mentions the number of fatalities and injured people, which are also mentioned in the premise
if fatalities_hypothesis != fatalities_premise:
    # check if the number of fatalities in the hypothesis contradicts the number of fatalities reported in the premise
    label = "contradiction"
elif injured_hypothesis != injured_premise:
    # check if the number of injured people from the hypothesis contradicts the number of injured people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
