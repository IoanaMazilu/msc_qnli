T_premise = 20
T_hypothesis = 20

# the hypothesis refers to the value of T mentioned in the premise
if T_hypothesis!= T_premise:
    # check if the value of T in the hypothesis contradicts the value of T reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
