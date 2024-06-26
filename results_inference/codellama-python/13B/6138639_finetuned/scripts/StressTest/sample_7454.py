T_premise = 105
T_hypothesis = 5/9 * (K-32)

# the hypothesis refers to the value of T mentioned in the premise
if T_premise <= T_hypothesis:
    # check if the estimate of 'T_hypothesis' contradicts the value of T in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
