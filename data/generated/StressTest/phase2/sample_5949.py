# Premise: If T = 5/9 * (K-32), and if T = 20, then what is the value of K?
# Hypothesis: If T = more than 2/9 * (K-32), and if T = 20, then what is the value of K?
# Golden Label: entailment

T_premise = 20
T_hypothesis = 20
K_premise = 5/9
K_hypothesis = 2/9

# The hypothesis refers to the same relationship between T and K as the premise, but with different coefficients
if T_hypothesis != T_premise:
    # Check if the value of T in the hypothesis contradicts the value of T in the premise
    label = "contradiction"
elif K_hypothesis >= K_premise:
    # Check if the coefficient of K in the hypothesis contradicts the coefficient of K in the premise
    label = "contradiction"
else:
    # The premise only gives an exact relationship between T and K.
    # Any relationship between T and K with a coefficient for K smaller than 'K_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

