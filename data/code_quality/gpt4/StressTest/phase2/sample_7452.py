T_premise = 105
T_hypothesis = 105
coef_premise = 5/9
coef_hypothesis = 4/9

# K is calculated from the equation T = coef * (K-32), given T
K_premise = (T_premise / coef_premise) + 32
K_hypothesis = (T_hypothesis / coef_hypothesis) + 32

# the hypothesis refers to the value of K calculated from the same equation
if K_hypothesis < K_premise:
    # check if the value of K calculated from the hypothesis contradicts the value of K calculated from the premise
    label = "contradiction"
elif coef_hypothesis != coef_premise:
    # check if the coefficient in the hypothesis contradicts the coefficient in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
