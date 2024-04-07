# Premise: If T = more than 1/9 * (K-32), and if T = 35, then what is the value of K?
# Hypothesis: If T = 5/9 * (K-32), and if T = 35, then what is the value of K?
# Golden Label: neutral

t_value_premise = 35
t_coefficient_premise = 1/9
t_value_hypothesis = 35
t_coefficient_hypothesis = 5/9

# the hypothesis refers to the same equation as in the premise, but with a different coefficient for T
if t_coefficient_hypothesis <= t_coefficient_premise:
    # check if the hypothesis coefficient contradicts the estimate of more than 't_coefficient_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the coefficient of T
    # any coefficient of T greater than 't_coefficient_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

