adults_premise = 2
children_premise = 2
adults_hypothesis = 2
children_hypothesis = 2

# the hypothesis mentions the number of adults and children from Sweden, which are also mentioned in the premise
if adults_hypothesis != adults_premise:
    # check if the number of adults in the hypothesis contradicts the number of adults reported in the premise
    label = "contradiction"
elif children_hypothesis != children_premise:
    # check if the number of children from the hypothesis contradicts the number of children in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
