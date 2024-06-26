T_premise = 105
T_hypothesis = 105
K_premise = (T_premise * 9/5) + 32
K_hypothesis = (T_hypothesis * 9/5) + 32

# the hypothesis refers to the same situation as the premise, but with a different condition
if T_hypothesis >= T_premise:
    # check if the condition of 'T_hypothesis' contradicts the condition of 'T_premise'
    label = "contradiction"
elif K_hypothesis!= K_premise:
    # check if the calculated value of 'K_hypothesis' contradicts the calculated value of 'K_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
