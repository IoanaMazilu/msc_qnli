# Premise: If T = more than 1/9 * (K-32), and if T = 75, then what is the value of K?
# Hypothesis: If T = 5/9 * (K-32), and if T = 75, then what is the value of K?
# Golden Label: neutral

T_premise = 75
T_hypothesis = 75
K_premise = (9 * T_premise) + 32
K_hypothesis = (9/5 * T_hypothesis) + 32

# the hypothesis and premise both refer to the same variables T and K
if K_premise != K_hypothesis:
    # check if the calculated value of K in the hypothesis contradicts the calculated value of K in the premise
    label = "contradiction"
else:
    # if the calculated value of K in the hypothesis does not contradict the calculated value of K in the premise
    # we cannot infer entailment, because the equations used to calculate K are different
    label = "neutral"

print(label)

