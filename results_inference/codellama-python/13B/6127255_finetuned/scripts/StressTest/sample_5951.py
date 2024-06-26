T_premise = 20
T_hypothesis = 20
K_premise = (T_premise * (9/5)) + 32
K_hypothesis = (T_hypothesis * (9/5)) + 32

# the hypothesis refers to the same situation as the premise, but with a different equation
if K_hypothesis >= K_premise:
    # check if the value of K in the hypothesis contradicts the value of K calculated from the premise
    label = "contradiction"
else:
    # the premise gives the exact value of K, but the hypothesis gives only an estimate
    # the hypothesis value is less than the premise value, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
