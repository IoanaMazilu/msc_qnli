fatalities_premise = 4
fatalities_hypothesis = 5

# the hypothesis mentions the number of infant deaths linked to the recliners, which is also mentioned in the premise
if fatalities_hypothesis > fatalities_premise:
    # check if the number of fatalities in the hypothesis contradicts the number of fatalities reported in the premise
    label = "contradiction"
else:
    # if the number of fatalities in the hypothesis does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
