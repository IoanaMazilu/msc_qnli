burned_acres_premise = 56000
burned_acres_hypothesis = 56000

# the hypothesis mentions the burned acres of the High Park Fire, which is also referenced in the premise
if burned_acres_hypothesis!= burned_acres_premise:
    # check if the burned acres in the hypothesis contradicts the burned acres reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
