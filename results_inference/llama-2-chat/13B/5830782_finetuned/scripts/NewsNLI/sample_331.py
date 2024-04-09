acres_consumed_premise = 56000
acres_consumed_hypothesis = 56000

# the hypothesis mentions the number of acres consumed by the fire, which is also mentioned in the premise
if acres_consumed_hypothesis!= acres_consumed_premise:
    # check if the number of acres consumed in the hypothesis contradicts the number of acres consumed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
