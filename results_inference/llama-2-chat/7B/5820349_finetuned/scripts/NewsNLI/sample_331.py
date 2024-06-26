acres_consumed_premise = 56000
acres_burned_hypothesis = 56000

# the hypothesis mentions the number of acres burned by the High Park Fire, which is also mentioned in the premise
if acres_burned_hypothesis!= acres_consumed_premise:
    # check if the number of acres burned in the hypothesis contradicts the number of acres consumed in the premise
    label = "contradiction"
else:
    # if the number of acres burned in the hypothesis does not contradict the number of acres consumed in the premise, we can infer entailment
    label = "entailment"

print(label)
