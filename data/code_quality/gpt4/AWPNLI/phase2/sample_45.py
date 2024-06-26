original_houses_premise = 20817.0
built_houses_premise = 97741.0
total_houses_hypothesis = 118560.0

# the hypothesis refers to the total number of houses, which are also mentioned in the premise
# compute the total number of houses in the premise
total_houses_premise = original_houses_premise + built_houses_premise
if total_houses_hypothesis != total_houses_premise:
    # check if the number of houses in the hypothesis contradicts the number of houses from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
