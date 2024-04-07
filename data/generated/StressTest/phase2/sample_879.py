# Premise: If T = 5/9 * (K-32), and if T = 35, then what is the value of K?
# Hypothesis: If T = more than 1/9 * (K-32), and if T = 35, then what is the value of K?
# Golden Label: entailment

T_premise = 35
T_hypothesis = 35
K_premise = (T_premise/(5/9)) + 32
K_hypothesis = (T_hypothesis/(1/9)) + 32

# the hypothesis refers to the same variable T and K mentioned in the premise
if T_hypothesis != T_premise:
    # check if the value of T in the hypothesis contradicts the value of T in the premise
    label = "contradiction"
elif K_hypothesis <= K_premise:
    # check if the calculated K value in the hypothesis contradicts the calculated K value in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the K value
    # any K value greater than 'K_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

