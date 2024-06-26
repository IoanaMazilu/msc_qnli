people_arrested_premise = 52
people_arrested_hypothesis = 52

# the hypothesis mentions the number of people arrested in Philadelphia, which is also mentioned in the premise
if people_arrested_hypothesis != people_arrested_premise:
    # check if the number of people arrested in the hypothesis contradicts the number of people arrested in the premise
    label = "contradiction"
else:
    # if the number of people arrested in the hypothesis does not contradict the number of people arrested in the premise, we can infer entailment
    label = "entailment"

print(label)
