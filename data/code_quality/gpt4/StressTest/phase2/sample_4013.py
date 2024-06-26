death_rate_premise = 5
death_rate_hypothesis = 1
leaving_rate = 15

# the hypothesis refers to the death and leaving rates in a village mentioned in the premise
if death_rate_hypothesis > death_rate_premise:
    # check if the death rate in the hypothesis contradicts the death rate reported in the premise
    label = "contradiction"
elif death_rate_hypothesis < death_rate_premise:
    # if the death rate in the hypothesis is less than that in the premise, it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the death rate in the hypothesis does not contradict the death rate in the premise, we can infer entailment
    label = "entailment"

print(label)
