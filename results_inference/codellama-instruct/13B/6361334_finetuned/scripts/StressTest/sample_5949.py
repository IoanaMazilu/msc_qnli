T_premise = 20
T_hypothesis = 20
K_premise = 5/9 * (K_hypothesis - 32)
K_hypothesis = K_premise + 2/9 * (K_hypothesis - 32)

# the hypothesis refers to the value of K, which is also mentioned in the premise
if K_hypothesis <= K_premise:
    # check if the estimate of 'K_hypothesis' contradicts the value of K in the premise
    label = "contradiction"
elif T_hypothesis!= T_premise:
    # check if the value of T in the hypothesis contradicts the value of T reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
