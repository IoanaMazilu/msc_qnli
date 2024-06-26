T_premise = 35
T_hypothesis = 35
K_premise = (T_premise * (9/5)) + 32
K_hypothesis = (T_hypothesis * (9/3)) + 32

# the hypothesis refers to the same situation as the premise, but with a different formula
if K_premise != K_hypothesis:
    # check if the calculated value of K in the hypothesis contradicts the calculated value of K in the premise
    label = "contradiction"
else:
    # if the calculated values of K are the same in premise and hypothesis, we can infer entailment
    label = "entailment"

print(label)
