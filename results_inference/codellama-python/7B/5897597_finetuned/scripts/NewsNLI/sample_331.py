acres_burned_premise = 56000
acres_burned_hypothesis = 56000

# the hypothesis mentions the area burned by the High Park Fire, which is also mentioned in the premise
if acres_burned_hypothesis!= acres_burned_premise:
    # check if the area burned in the hypothesis contradicts the area burned reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
