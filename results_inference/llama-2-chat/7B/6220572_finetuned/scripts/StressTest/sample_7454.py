T_premise = 5/9 * (K-32)
T_hypothesis = 5/9 * (K-32)
T_value_premise = 105
T_value_hypothesis = 105

# the hypothesis refers to the condition of the value of T in the premise
if T_premise <= T_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'T_premise'
    label = "contradiction"
elif T_value_hypothesis!= T_value_premise:
    # check if the value of T in the hypothesis contradicts the value of T reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
