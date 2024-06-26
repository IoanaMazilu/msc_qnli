original_houses_premise = 20817.0
current_houses_premise = 97741.0
houses_built_hypothesis = 76923.0

# the hypothesis refers to the number of houses built, which can be estimated from the premise
# compute the number of houses built in the premise
houses_built_premise = current_houses_premise - original_houses_premise

if houses_built_hypothesis != houses_built_premise:
    # check if the number of houses built in the hypothesis contradicts the number of houses built from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
