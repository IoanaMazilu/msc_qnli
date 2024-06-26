T_premise = 105
T_hypothesis = 105
K_premise = (T_premise / (5/9)) + 32
K_hypothesis = (T_hypothesis / (4/9)) + 32

# the hypothesis refers to the value of K when T = 105, which is also mentioned in the premise
if K_premise!= K_hypothesis:
    # check if the calculated value of K in the hypothesis contradicts the calculated value of K in the premise
    label = "contradiction"
else:
    # if the calculated value of K in the hypothesis does not contradict the calculated value of K in the premise, we can infer entailment
    label = "entailment"

print(label)
