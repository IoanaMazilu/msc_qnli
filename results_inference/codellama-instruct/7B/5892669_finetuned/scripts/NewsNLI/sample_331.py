acres_burned_premise = 56000
acres_burned_hypothesis = 56000

# the hypothesis mentions the number of acres burned, which is also referenced in the premise
if acres_burned_hypothesis!= acres_burned_premise:
    # check if the number of acres burned in the hypothesis contradicts the number of acres burned reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
