# Premise: If T = 5/9 * (K-32), and if T = 50, then what is the value of K?
# Hypothesis: If T = less than 6/9 * (K-32), and if T = 50, then what is the value of K?
# Golden Label: entailment

T_premise = 50
T_hypothesis = 50
T_formula_premise = 5/9
T_formula_hypothesis = 6/9

# the hypothesis refers to the formula of T mentioned in the premise
if T_premise != T_hypothesis:
    # check if the value of T in the hypothesis contradicts the value of T in the premise
    label = "contradiction"
elif T_formula_premise >= T_formula_hypothesis:
    # check if the formula for T in the hypothesis contradicts the formula for T in the premise
    label = "contradiction"
else:
    # the formula in the premise gives an exact calculation for T
    # any formula less than 'T_formula_premise' cannot be explicitly entailed from the premise and does not contradict it either
    label = "neutral"

print(label)

