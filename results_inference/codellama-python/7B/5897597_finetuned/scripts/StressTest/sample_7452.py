T_premise = 105
T_hypothesis = 105

# the hypothesis refers to the value of T mentioned in the premise
if T_hypothesis!= T_premise:
    # check if the value of 'T_hypothesis' contradicts the value of T in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
