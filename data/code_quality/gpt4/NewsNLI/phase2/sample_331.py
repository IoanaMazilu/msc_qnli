acres_burned_premise = 56000
acres_burned_hypothesis = 56000

# the hypothesis mentions the number of burned acres, which is also mentioned in the premise
if acres_burned_hypothesis != acres_burned_premise:
    # check if the number of burned acres in the hypothesis contradicts the number of burned acres reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
