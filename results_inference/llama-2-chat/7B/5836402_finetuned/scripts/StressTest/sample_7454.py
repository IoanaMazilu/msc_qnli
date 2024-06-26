T_value_premise = 105
T_value_hypothesis = 105

# the hypothesis refers to the same T value and the equation mentioned in the premise
if T_value_premise >= (5/9) * (K-32):
    # check if the value of T in the hypothesis contradicts the estimate of less than '(5/9) * (K-32)'
    label = "contradiction"
elif T_value_premise <= (5/9) * (K-32):
    # check if the value of T in the hypothesis contradicts the estimate of more than '(5/9) * (K-32)'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
