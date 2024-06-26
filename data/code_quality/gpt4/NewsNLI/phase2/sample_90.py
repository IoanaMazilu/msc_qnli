deaths_premise = 3
deaths_hypothesis = 3

# the hypothesis mentions the number of deaths due to the storm, which is also mentioned in the premise
if deaths_hypothesis != deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the number of deaths in the hypothesis does not contradict the number of deaths in the premise, we can infer entailment
    label = "entailment"

print(label)
