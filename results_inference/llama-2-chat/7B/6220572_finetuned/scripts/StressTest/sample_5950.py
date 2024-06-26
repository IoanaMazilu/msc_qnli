T_premise = 2/9 * (K-32)
T_hypothesis = 5/9 * (K-32)
K_premise = 32
K_hypothesis = 20

# the hypothesis refers to the conditions and the value of K mentioned in the premise
if T_hypothesis!= T_premise:
    # check if the hypothesis value contradicts the estimate of 'T_premise'
    label = "contradiction"
elif K_hypothesis!= K_premise:
    # check if the hypothesis value contradicts the value of K reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
