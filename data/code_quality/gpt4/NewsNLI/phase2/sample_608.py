acres_burned_premise = 100000
acres_burned_hypothesis = 100000

# the hypothesis mentions the number of acres burned, which is also referenced in the premise
if acres_burned_hypothesis != acres_burned_premise:
    # check if the number of acres burned in the hypothesis contradicts the number of acres burned in the premise
    label = "contradiction"
else:
    # if the number of acres burned in the hypothesis does not contradict the number of acres burned in the premise, we can infer entailment
    label = "entailment"

print(label)
