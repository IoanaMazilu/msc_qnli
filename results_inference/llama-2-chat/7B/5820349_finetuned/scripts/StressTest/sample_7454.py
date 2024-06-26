T_premise = 105
T_hypothesis = 105
K_premise = (T_premise * 5/9) + 32
K_hypothesis = (T_hypothesis * 5/9) + 32

# the hypothesis refers to the same situation as the premise but with a different condition for T
if T_premise < T_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif K_premise!= K_hypothesis:
    # check if the calculated value of K in the hypothesis contradicts the calculated value of K in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
