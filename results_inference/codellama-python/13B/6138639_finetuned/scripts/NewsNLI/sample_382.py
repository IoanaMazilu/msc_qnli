deaths_premise = 9
deaths_hypothesis = 9

# the hypothesis mentions the number of deaths in El Salvador, which is also mentioned in the premise
if deaths_hypothesis!= deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)