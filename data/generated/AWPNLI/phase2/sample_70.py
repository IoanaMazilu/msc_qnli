# Premise: A restaurant made 9.0 hamburgers and 4.0 hot dogs to serve during lunch and only 3.0 hamburgers were actually served.
# Hypothesis: 6.0 hamburgers were left over.
# Golden Label: entailment

made_hamburgers_premise = 9.0
served_hamburgers_premise = 3.0
leftover_hamburgers_hypothesis = 6.0

# the hypothesis refers to the number of leftover hamburgers, which can be calculated from the premise
# compute the number of leftover hamburgers in the premise
leftover_hamburgers_premise = made_hamburgers_premise - served_hamburgers_premise
if leftover_hamburgers_hypothesis != leftover_hamburgers_premise:
    # check if the number of leftover hamburgers in the hypothesis contradicts the number of leftover hamburgers from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

