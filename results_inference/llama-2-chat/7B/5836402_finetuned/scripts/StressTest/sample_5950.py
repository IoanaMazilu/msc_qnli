T_premise = 2/9 * (K-32)
T_hypothesis = 5/9 * (K-32)
T_premise_value = 20
T_hypothesis_value = 20

# the hypothesis talks about the value of T mentioned in the premise
if T_hypothesis_value!= T_premise_value:
    # check if the value of T in the hypothesis contradicts the value of T reported in the premise
    label = "contradiction"
elif T_premise!= T_hypothesis:
    # check if the value of T in the premise contradicts the value of T in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
